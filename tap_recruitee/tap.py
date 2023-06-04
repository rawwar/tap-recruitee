"""recruitee tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th

from tap_recruitee import streams


class Taprecruitee(Tap):
    """recruitee tap class."""

    name = "tap-recruitee"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "auth_token",
            th.StringType,
            required=True,
            secret=True,  # Flag config as protected.
            description="The token to authenticate against the API service",
        ),
        th.Property(
            "company_id",
            th.IntegerType,
            required=True,
            description="Company id",
        ),
        th.Property(
            "api_url",
            th.StringType,
            required=False,
            description="API URL for tap recruitee",
            default="https://api.recruitee.com",
        ),
    ).to_dict()

    def discover_streams(self) -> list[streams.RecruiteeStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            streams.CandidateStream(self),
            streams.OfferStream(self),
            streams.DepartmentsStream(self),
        ]


if __name__ == "__main__":
    Taprecruitee.cli()
