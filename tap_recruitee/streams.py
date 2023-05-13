"""Stream type classes for tap-recruitee."""

from __future__ import annotations

from tap_recruitee import schemas
from tap_recruitee.client import RecruiteeStream


class CandidateStream(RecruiteeStream):
    """Define custom stream."""

    name = "candidates"
    path = "/candidates"
    primary_keys = ["id"]
    schema = schemas.candidates
    records_jsonpath = "$.candidates[*]"
