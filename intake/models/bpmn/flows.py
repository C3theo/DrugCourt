# from viewflow import flow, frontend
# from viewflow.base import this, Flow
# from viewflow.flow.views import CreateProcessView, UpdateProcessView

# from intake import views
# from .bpmn import DynamicSplitProcess
# from .nodes import DynamicSplit


# class DecisionFlow(Flow):

#     process_class = DynamicSplitProcess

#     # start = (
#     #     flow.Start(
#     #         CreateProcessView,
#     #         fields=['question', 'split_count'],
#     #         task_result_summary="Asks for {{ process.split_count }} decisions")
#     #     .Permission(auto_create=True)
#     #     .Next(this.split_on_decision)
#     # )

#     start = flow.StartFunction().Next(this.split_on_decision)

#     split_on_decision = (
#         DynamicSplit(lambda p: 4)
#         .IfNone(this.end)
#         .Next(this.make_decision)
#     )

#     make_decision = (
#         flow.View(
#             views.DecisionCreateView,
#             task_description="Decision required")
#         .Next(this.join_on_decision)
#     )

#     join_on_decision = flow.Join().Next(this.end)

#     end = flow.End()

#     # flow.Split().Next()

#     # start = (
#     #     flow.View(DecisionView).If(
#     #         lambda user_role: check_user_role_not_assigned).Then(this.approve_approve)

#     #     # Assign(check_user_role_not_assigned)
#     # )

#     # flow.Join(self)

#     # end = flow.End()

#     # def approve_decision(self):
        
#         # this.DecisionProcess.objects.
#         # how to get Decision Process instance reference
