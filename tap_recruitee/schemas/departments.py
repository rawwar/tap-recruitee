"""Schema for Departments."""

from singer_sdk import typing as th

schema = th.PropertiesList(
    th.Property(
        "grouped_translations",
        th.ObjectType(
            th.Property(
                "de",
                th.ObjectType(
                    th.Property("name", th.StringType),
                ),
            ),
            th.Property(
                "en",
                th.ObjectType(
                    th.Property("name", th.StringType),
                ),
            ),
        ),
    ),
    th.Property("id", th.IntegerType),
    th.Property("name", th.StringType),
    th.Property("offers_count", th.IntegerType),
    th.Property("status", th.StringType),
)

schema_dict = schema.to_dict()
