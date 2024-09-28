class GreekNameProcessor:
    def get_klitiki(self, name):
        try:
            """
            Converts a given Greek name to its Klitiki (vocative) form based on specific suffix rules.
            """
            if name.endswith('ης'):
                return name.removesuffix('ς')
            elif name.endswith('ής'):
                return name.removesuffix('ς')
            elif name.endswith('ων'):
                return name + 'α'
            elif name.endswith('ας'):
                return name.removesuffix('ας') + 'α'
            elif name.endswith('ις'):
                return name.removesuffix('ς')
            elif name.endswith('γος'):
                return name.removesuffix('ς')
            elif name.endswith('σος'):
                return name.removesuffix('ς')
            elif name.endswith('κος'):
                return name.removesuffix('ς')
            elif name.endswith('ος'):
                return name.removesuffix('ος') + 'ε'
            elif name.endswith('ός'):
                return name.removesuffix('ός') + 'έ'
            else:
                return name
        except Exception as e:
            print(f"Error processing name '{name}': {e}")
            return name

    def process_names(self, names):
        processed = []
        for name in names:
            name = self.get_klitiki(name)
            processed.append(name)
        return processed
    

    def process_name(self, name):
        return self.get_klitiki(name)