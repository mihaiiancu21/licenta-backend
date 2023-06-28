import openai
from rest_framework import generics, status
from rest_framework.response import Response

from BrainQuest.settings import CHAT_GPT_API_KEY

openai.api_key = CHAT_GPT_API_KEY.strip()


class ChatGPTView(generics.ListCreateAPIView):
    """
    Compile/Execute code for user for a small defined amount of testcases
    This is used more for users to test if their code it is working and has no errors
    """

    def create(self, request, *args, **kwargs):
        try:
            # content_message = f"Give me some improvements for " \
            #                   f"this code\n\n\n {request.data['user_code']}"
            #
            # messages = [
            #     {"role": "user", "content": content_message}
            # ]
            #
            # completion = openai.ChatCompletion.create(
            #     model="gpt-3.5-turbo",
            #     messages=messages
            # )
            #
            # results = {
            #     "code_improvements": completion.choices[0].message.content
            # }

            a = """Here are some potential improvements to the code:

1. Use the formula for the sum of an arithmetic series: The current code sums the first n positive integers using the built-in `sum()` function and the `range()` function. However, there is a formula for the sum of an arithmetic series (i.e., a series where each term is obtained by adding a fixed constant to the previous term). The formula is:

    sum = n * (n + 1) / 2

   This formula can be used to compute the sum more efficiently than iterating over all the numbers in the range. Here's how the code would look with this change:

   ```python
   def seriesSum(self, n):
       s = n * (n + 1) / 2
       return s
   ```

2. Add input validation: The current code assumes that the input `n` is a positive integer. However, it doesn't check whether this assumption is true. To make the function more robust, you could add some input validation to check that `n` is indeed a positive integer. Here's an example of how you might do this:

   ```python
   def seriesSum(self, n):
       if not isinstance(n, int) or n <= 0:
           raise ValueError("n must be a positive integer")
       s = n * (n + 1) / 2
       return s
   ```

3. Rename the function: The function is currently called `seriesSum`, which doesn't give a lot of information about what the function is doing. A more descriptive name might be `sum_of_first_n_positive_integers`. Here's how you could rename the function:

   ```python
   def sum_of_first_n_positive_integers(self, n):
       if not isinstance(n, int) or n <= 0:
           raise ValueError("n must be a positive integer")
       s = n * (n + 1) / 2
       return s
   ```

These are just a few suggestions; depending on the context in which this code is being used, there may be other improvements you could make to make the code more e"""

            results = {
                "code_improvements": a
            }

            return Response(data=results, status=status.HTTP_200_OK)
        except Exception as exc:

            results = {
                "code_improvements": f"Something went wrong communicating with AI model. "
                                     f"Reason {str(exc)}"
            }

            return Response(data=results, status=status.HTTP_200_OK)
