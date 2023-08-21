# Calculator_steps.py

class Calculator:
    def add(self, *args):
        if len(args) > 3:
            return None
        if any(not isinstance(x, int) for x in args):
            return None
        if any(x > 100 for x in args):
            return None
        return sum(args)
