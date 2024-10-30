from rest_framework.exceptions import NotFound

from hire_center.models import Candidate
from hire_center.serializers import CandidateSerializer


class CandidateService:
    @classmethod
    def get_list(cls, company_id):
        return Candidate.objects.filter(company_id=company_id)

    @classmethod
    def create(cls, data, company_id):
        data["company"] = company_id
        serializer = CandidateSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer

    @classmethod
    def read(cls, pk, company_id):
        try:
            return Candidate.objects.get(pk=pk, company_id=company_id)
        except Candidate.DoesNotExist:
            raise NotFound("Candidate not found")

    @classmethod
    def update(cls, pk, data, company_id):
        data["company"] = company_id
        candidate = cls.read(pk, company_id)
        serializer = CandidateSerializer(candidate, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer

    @classmethod
    def delete(cls, pk, company_id):
        candidate = cls.read(pk, company_id)
        candidate.delete()
