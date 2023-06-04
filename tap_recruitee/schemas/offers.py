"""Schema for Offers."""

from singer_sdk import typing as th

schema = th.PropertiesList(
    th.Property("kind", th.StringType),
    th.Property("qualified_candidates_count", th.IntegerType),
    th.Property("hiring_manager_id", th.StringType),
    th.Property("status", th.StringType),
    th.Property("published_at", th.StringType),
    th.Property(
        "issues",
        th.ObjectType(
            th.Property("is_required_data_missing", th.BooleanType),
            th.Property("is_requisition_missing", th.BooleanType),
        ),
    ),
    th.Property("disqualified_candidates_count", th.IntegerType),
    th.Property("careers_url", th.StringType),
    th.Property("id", th.IntegerType),
    th.Property(
        "pipeline_template",
        th.ObjectType(
            th.Property("category", th.StringType),
            th.Property("custom", th.BooleanType),
            th.Property("default", th.BooleanType),
            th.Property("id", th.IntegerType),
            th.Property("position", th.IntegerType),
            th.Property("requires_adjustment", th.BooleanType),
            th.Property(
                "stages",
                th.ArrayType(
                    th.ObjectType(
                        th.Property(
                            "action_templates",
                            th.ArrayType(
                                th.ObjectType(
                                    th.Property(
                                        "data",
                                        th.ObjectType(
                                            th.Property(
                                                "tags",
                                                th.ArrayType(th.StringType),
                                            ),
                                        ),
                                    ),
                                    th.Property("id", th.IntegerType),
                                    th.Property("kind", th.StringType),
                                    th.Property(
                                        "references",
                                        th.ArrayType(th.StringType),
                                    ),
                                ),
                            ),
                        ),
                        th.Property("category", th.StringType),
                        th.Property("fair_evaluations_enabled", th.BooleanType),
                        th.Property("group", th.StringType),
                        th.Property("id", th.IntegerType),
                        th.Property("locked", th.BooleanType),
                        th.Property("name", th.StringType),
                        th.Property("placements_count", th.IntegerType),
                        th.Property("position", th.IntegerType),
                        th.Property("time_limit", th.StringType),
                    ),
                ),
            ),
            th.Property("title", th.StringType),
        ),
    ),
    th.Property("candidates_count", th.IntegerType),
    th.Property("hired_candidates_without_openings_count", th.IntegerType),
    th.Property("street", th.StringType),
    th.Property("job_scheduler", th.StringType),
    th.Property("number_of_openings", th.IntegerType),
    th.Property("eeo_settings", th.StringType),
    th.Property("followed", th.BooleanType),
    th.Property("state_name", th.StringType),
    th.Property("title", th.StringType),
    th.Property(
        "enabled_languages",
        th.ArrayType(
            th.ObjectType(
                th.Property("code", th.StringType),
                th.Property("name", th.StringType),
                th.Property("native_name", th.StringType),
            ),
        ),
    ),
    th.Property("url", th.StringType),
    th.Property("location", th.StringType),
    th.Property("closed_at", th.StringType),
    th.Property("adminapp_url", th.StringType),
    th.Property("followers", th.ArrayType(th.StringType)),
    th.Property("guid", th.StringType),
    th.Property("has_active_campaign", th.BooleanType),
    th.Property("department_id", th.StringType),
    th.Property("city", th.StringType),
    th.Property("department", th.StringType),
    th.Property("position", th.IntegerType),
    th.Property("example", th.BooleanType),
    th.Property("employment_type", th.StringType),
    th.Property("updated_at", th.StringType),
    th.Property("offer_tags", th.ArrayType(th.StringType)),
    th.Property("created_at", th.StringType),
    th.Property("hired_candidates_count", th.IntegerType),
    th.Property("recruiter_id", th.StringType),
    th.Property("slug", th.StringType),
    th.Property("lang_code", th.StringType),
    th.Property("state_code", th.StringType),
    th.Property("enabled_for_referrals", th.BooleanType),
    th.Property("mailbox_email", th.StringType),
    th.Property("pipeline", th.BooleanType),
    th.Property("postal_code", th.StringType),
    th.Property("shared_openings_count", th.IntegerType),
    th.Property("country_code", th.StringType),
)
schema_dict = schema.to_dict()
