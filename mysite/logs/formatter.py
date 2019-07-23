import logging

class SQLFormatter(logging.Formatter):
    def format(self, record):
        # import pdb; pdb.set_trace()
        # Check if Pygments is available for coloring
        try:
            import pygments
            from pygments.lexers import SqlLexer
            from pygments.formatters import TerminalTrueColorFormatter
        except ImportError:
            pygments = None

        # Check if sqlparse is available for indentation
        try:
            import sqlparse
        except ImportError:
            sqlparse = None

        # Remove leading and trailing whitespaces
        sql = record.sql.strip()

        if sqlparse:
            # Indent the SQL query
            sql = sqlparse.format(sql, reindent=True)

        if pygments:
            # Highlight the SQL query
            sql = pygments.highlight(
                sql,
                SqlLexer(),
                TerminalTrueColorFormatter(style='monokai')
            )

        # Set the record's statement to the formatted query
        record.statement = sql
        return super(SQLFormatter, self).format(record)


import logging, inspect

class ContextFilter(logging.Filter):
    """
    Injects stack trace information when added as a filter to a
    python logger
    """

    def filter(self, record):
        source_trace = ''

        stack = inspect.stack()
        for s in reversed(stack):
            line = s[2]
            file = '/'.join(s[1].split('/')[-3:])
            calling_method = s[3]
            source_trace += 'Line %s in %s at %s\n' % (line, file, calling_method)

        # pass to format string
        record.sourcetrace = source_trace

        # clean up
        del stack

        return True

django_db_backends_logger = logging.getLogger('django.db.backends')
f = ContextFilter()
django_db_backends_logger.addFilter(f)