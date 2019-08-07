# from viewflow import flow
# from viewflow.base import this, Flow
# from viewflow.flow.views import CreateProcessView, UpdateProcessView
from django.db import models
# from viewflow.models import Process
from model_utils import Choices

# from profiles.models import Profile

from django_fsm import (ConcurrentTransitionMixin, FSMField,
                        TransitionNotAllowed, transition)


# class DynamicSplitProcess(Process):
#     split_count = models.IntegerField(default=0)
