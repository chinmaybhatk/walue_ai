from . import __version__ as app_version

app_name = "walue_ai"
app_title = "Walue AI"
app_publisher = "Walue AI"
app_description = "AI-Powered Business Intelligence Platform"
app_email = "contact@walueai.com"
app_license = "MIT"

# Home Pages
# ----------

# application home page (will override Website Settings)
home_page = "home"

# Website Route Rules
# -------------------

website_route_rules = [
	{"from_route": "/home", "to_route": "home"},
]
