from fastapi import FastAPI

from fastf1 import FastAPI

app = FastAPI(title="IT Domain")

IT_data = [
    {"ToolName": "Git", "Category": "Version Control", "Critical": True, "Licensed": False},
    {"ToolName": "Docker", "Category": "Containerization", "Critical": True, "Licensed": False},
    {"ToolName": "Kubernetes", "Category": "Orchestration", "Critical": True, "Licensed": False},
    {"ToolName": "Jenkins", "Category": "CI/CD", "Critical": True, "Licensed": False},
    {"ToolName": "GitHub", "Category": "Code Hosting", "Critical": True, "Licensed": True},
    {"ToolName": "GitLab", "Category": "CI/CD", "Critical": True, "Licensed": True},
    {"ToolName": "Bitbucket", "Category": "Code Hosting", "Critical": False, "Licensed": True},
    {"ToolName": "Terraform", "Category": "Infrastructure as Code", "Critical": True, "Licensed": False},
    {"ToolName": "Ansible", "Category": "Configuration Management", "Critical": True, "Licensed": False},
    {"ToolName": "Helm", "Category": "Kubernetes Tooling", "Critical": False, "Licensed": False},

    {"ToolName": "Prometheus", "Category": "Monitoring", "Critical": True, "Licensed": False},
    {"ToolName": "Grafana", "Category": "Monitoring", "Critical": True, "Licensed": False},
    {"ToolName": "Datadog", "Category": "Monitoring", "Critical": True, "Licensed": True},
    {"ToolName": "New Relic", "Category": "Monitoring", "Critical": False, "Licensed": True},
    {"ToolName": "ElasticSearch", "Category": "Logging", "Critical": True, "Licensed": False},
    {"ToolName": "Logstash", "Category": "Logging", "Critical": False, "Licensed": False},
    {"ToolName": "Kibana", "Category": "Logging", "Critical": True, "Licensed": False},
    {"ToolName": "Splunk", "Category": "Logging", "Critical": True, "Licensed": True},
    {"ToolName": "Fluentd", "Category": "Logging", "Critical": False, "Licensed": False},
    {"ToolName": "Graylog", "Category": "Logging", "Critical": False, "Licensed": True},

    {"ToolName": "PostgreSQL", "Category": "Database", "Critical": True, "Licensed": False},
    {"ToolName": "MySQL", "Category": "Database", "Critical": True, "Licensed": False},
    {"ToolName": "Oracle DB", "Category": "Database", "Critical": True, "Licensed": True},
    {"ToolName": "SQL Server", "Category": "Database", "Critical": True, "Licensed": True},
    {"ToolName": "MongoDB", "Category": "Database", "Critical": True, "Licensed": False},
    {"ToolName": "Redis", "Category": "Caching", "Critical": True, "Licensed": False},
    {"ToolName": "Cassandra", "Category": "Database", "Critical": False, "Licensed": False},
    {"ToolName": "DynamoDB", "Category": "Database", "Critical": True, "Licensed": True},
    {"ToolName": "Snowflake", "Category": "Data Warehouse", "Critical": True, "Licensed": True},
    {"ToolName": "BigQuery", "Category": "Data Warehouse", "Critical": True, "Licensed": True},

    {"ToolName": "Apache Kafka", "Category": "Streaming", "Critical": True, "Licensed": False},
    {"ToolName": "RabbitMQ", "Category": "Messaging", "Critical": False, "Licensed": False},
    {"ToolName": "ActiveMQ", "Category": "Messaging", "Critical": False, "Licensed": True},
    {"ToolName": "Apache Spark", "Category": "Data Processing", "Critical": True, "Licensed": False},
    {"ToolName": "Apache Flink", "Category": "Streaming", "Critical": False, "Licensed": False},
    {"ToolName": "Airflow", "Category": "Workflow Orchestration", "Critical": True, "Licensed": False},
    {"ToolName": "Prefect", "Category": "Workflow Orchestration", "Critical": False, "Licensed": True},
    {"ToolName": "dbt", "Category": "Data Transformation", "Critical": True, "Licensed": False},
    {"ToolName": "Talend", "Category": "ETL", "Critical": False, "Licensed": True},
    {"ToolName": "Informatica", "Category": "ETL", "Critical": True, "Licensed": True},

    {"ToolName": "VS Code", "Category": "IDE", "Critical": True, "Licensed": False},
    {"ToolName": "PyCharm", "Category": "IDE", "Critical": False, "Licensed": True},
    {"ToolName": "IntelliJ IDEA", "Category": "IDE", "Critical": False, "Licensed": True},
    {"ToolName": "Eclipse", "Category": "IDE", "Critical": False, "Licensed": False},
    {"ToolName": "Jupyter", "Category": "Notebook", "Critical": True, "Licensed": False},
    {"ToolName": "Confluence", "Category": "Documentation", "Critical": True, "Licensed": True},
    {"ToolName": "Notion", "Category": "Documentation", "Critical": False, "Licensed": True},
    {"ToolName": "SharePoint", "Category": "Documentation", "Critical": True, "Licensed": True},
    {"ToolName": "Slack", "Category": "Communication", "Critical": True, "Licensed": True},
    {"ToolName": "Microsoft Teams", "Category": "Communication", "Critical": True, "Licensed": True},

    {"ToolName": "Okta", "Category": "Identity Management", "Critical": True, "Licensed": True},
    {"ToolName": "Keycloak", "Category": "Identity Management", "Critical": True, "Licensed": False},
    {"ToolName": "Vault", "Category": "Secrets Management", "Critical": True, "Licensed": False},
    {"ToolName": "AWS IAM", "Category": "Cloud Security", "Critical": True, "Licensed": True},
    {"ToolName": "Azure AD", "Category": "Cloud Security", "Critical": True, "Licensed": True},
    {"ToolName": "CloudWatch", "Category": "Monitoring", "Critical": True, "Licensed": True},
    {"ToolName": "Sentry", "Category": "Error Tracking", "Critical": True, "Licensed": True},
    {"ToolName": "PagerDuty", "Category": "Incident Management", "Critical": True, "Licensed": True},
    {"ToolName": "ServiceNow", "Category": "ITSM", "Critical": True, "Licensed": True},
    {"ToolName": "Jira", "Category": "Project Management", "Critical": True, "Licensed": True}
]
