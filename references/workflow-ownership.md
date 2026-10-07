# Workflow ownership

An explicit pstack invocation gives pstack ownership of that workflow. An explicit Superpowers invocation gives Superpowers ownership. Do not run both controllers over the same assignment or let one silently replace the other's plan, review, or integration decisions.

For an unqualified request, D1 retains the already active workflow. With no active workflow, use host defaults and do not activate either orchestration mode automatically. If both pstack and Superpowers are explicitly requested, clarify ownership before launching workers or changing artifacts. Preserve the active controller across follow-ups unless the user changes ownership. A helper skill can advise the owner without becoming a second controller.

The owner assigns one coordinator. Workers produce isolated artifacts and evidence; the coordinator reviews and integrates them. Shared inventory and registry writes belong to the coordinator. Worker cancellation, stale results or unavailable tools do not transfer that ownership automatically.

Host permissions and user authorization constrain every owner. Local structural tests, documented APIs and declared cases provide no host pass. Explicit reduced or blocked results remain visible beside the full expectation.
