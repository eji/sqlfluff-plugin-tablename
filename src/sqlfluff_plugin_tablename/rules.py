"""An example of a custom rule implemented through the plugin system.

This uses the rules API supported from 0.4.0 onwards.
"""

from sqlfluff.core.rules import (
    BaseRule,
    LintResult,
    RuleContext,
)
from sqlfluff.core.rules.crawlers import SegmentSeekerCrawler


# These two decorators allow plugins
# to be displayed in the sqlfluff docs
class Rule_TableName_L001(BaseRule):
    """ORDER BY on these columns is forbidden!

    **Anti-pattern**

    Using ``ORDER BY`` one some forbidden columns.

    .. code-block:: sql

        SELECT *
        FROM foo
        ORDER BY
            bar,
            baz

    **Best practice**

    Do not order by these columns.

    .. code-block:: sql

        SELECT *
        FROM foo
        ORDER BY bar
    """

    groups = ("all",)
    config_keywords = ["table_name"]
    crawl_behaviour = SegmentSeekerCrawler({"create_table_statement"}) # fixme
    is_fix_compatible = True

    def _eval(self, context: RuleContext):
        """We should not ORDER BY forbidden_columns."""
        for seg in context.segment.segments:
            col_name = seg.raw.lower()
            print("--------------------")
            print(col_name)
            print("--------------------")

        return LintResult(
            description="test description",
        )