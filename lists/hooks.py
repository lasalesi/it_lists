# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "lists"
app_title = "Lists"
app_publisher = "Mangrova Technologies"
app_description = "Extension module for lists"
app_icon = "octicon octicon-database"
app_color = "blue"
app_email = "lars.mueller@sunrise.ch"
app_license = "GPL"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/lists/css/lists.css"
# app_include_js = "/assets/lists/js/lists.js"

# include js, css files in header of web template
# web_include_css = "/assets/lists/css/lists.css"
# web_include_js = "/assets/lists/js/lists.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "lists.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "lists.install.before_install"
# after_install = "lists.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "lists.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"lists.tasks.all"
# 	],
# 	"daily": [
# 		"lists.tasks.daily"
# 	],
# 	"hourly": [
# 		"lists.tasks.hourly"
# 	],
# 	"weekly": [
# 		"lists.tasks.weekly"
# 	]
# 	"monthly": [
# 		"lists.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "lists.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "lists.event.get_events"
# }

