class CodeValidator:

    @staticmethod
    def validate(code):

        try:

            compile(code, "<generated>", "exec")

            return True, None

        except Exception as e:

            return False, str(e)