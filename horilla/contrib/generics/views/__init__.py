"""
Horilla generics views package.

Aggregates generic list, detail, form, kanban, group-by, and helper views.
Import order is significant to avoid circular imports.
"""

from horilla.contrib.generics.views.core import *
from horilla.contrib.generics.views.delete import *
from horilla.contrib.generics.views.helpers.condition_widget import *
from horilla.contrib.generics.views.details import *
from horilla.contrib.generics.views.list import *
from horilla.contrib.generics.views.card import *
from horilla.contrib.generics.views.split_view import *
from horilla.contrib.generics.views.detail_tabs import *
from horilla.contrib.generics.views.groupby import *
from horilla.contrib.generics.views.chart import *
from horilla.contrib.generics.views.kanban import *
from horilla.contrib.generics.views.timeline import *
from horilla.contrib.generics.views import helpers
from horilla.contrib.generics.views.attachments import *
from horilla.contrib.generics.views.global_search import *
from horilla.contrib.generics.views.related_list import *
from horilla.contrib.generics.views.single_form import *
from horilla.contrib.generics.views.multi_form import *
from horilla.contrib.generics.views.navbar import *
