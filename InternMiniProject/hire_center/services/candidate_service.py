import os

import requests
from rest_framework.exceptions import NotFound

from hire_center.models import Candidate
from hire_center.serializers import CandidateSerializer

slack_hook = os.environ.get("SLACK_WEBHOOK_URL")


def notify_slack(data):
    url = slack_hook
    requests.post(url, json=data)


def get_candidate_list(company_id):
    return Candidate.objects.filter(company_id=company_id)


def create_candidate(data, company_id):
    data["company"] = company_id
    serializer = CandidateSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    candidate = serializer.save()
    notify_slack(
        {"text": "New candidate created, contact: {}".format(candidate.contact)}
    )
    return serializer


def read_candidate(pk, company_id):
    try:
        return Candidate.objects.get(pk=pk, company_id=company_id)
    except Candidate.DoesNotExist:
        raise NotFound("Candidate not found")


def update_candidate(pk, data, company_id):
    data["company"] = company_id
    candidate = read_candidate(pk, company_id)
    serializer = CandidateSerializer(candidate, data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return serializer


def delete_candidate(pk, company_id):
    candidate = read_candidate(pk, company_id)
    candidate.delete()
