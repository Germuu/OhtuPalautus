class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def _stringify_list(self, items):
        # Returns a bulleted list or a single dash if empty
        return "\n".join(f"- {item}" for item in items) if items else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}"
            f"\n\nAuthors:\n" + self._stringify_list(self.authors or ["-"])
            + f"\n\nDependencies:\n" + self._stringify_list(self.dependencies)
            + f"\n\nDevelopment dependencies:\n" + self._stringify_list(self.dev_dependencies)
        )
