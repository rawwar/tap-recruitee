"""Stream type classes for tap-recruitee."""

from __future__ import annotations

from tap_recruitee import schemas
from tap_recruitee.client import RecruiteeStream


class CandidateStream(RecruiteeStream):
    """Candidates stream."""

    name = "candidates"
    path = "/candidates"
    primary_keys = ["id"]
    schema = schemas.candidates
    records_jsonpath = "$.candidates[*]"


class OfferStream(RecruiteeStream):
    """Offer stream."""

    name = "offers"
    path = "/offers"
    primary_keys = ["id"]
    schema = schemas.offers
    records_jsonpath = "$.offers[*]"


class DepartmentsStream(RecruiteeStream):
    """Departments stream."""

    name = "departments"
    path = "/departments"
    primary_keys = ["id"]
    schema = schemas.departments
    records_jsonpath = "$.departments[*]"
