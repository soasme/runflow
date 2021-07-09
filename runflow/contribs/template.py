class Hcl2TemplateTask:
    """Render HCL2 template.

    Note: this class is just a placeholder class for hcl2 task system
    to work. The actual implementation is on `runflow.core`.
    """

    def __init__(self, source, context=None):
        self.source = source

    async def run(self):
        return {"content": self.source}
