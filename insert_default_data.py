import os
import sys

sys.path.append("BrainQuest")
os.environ["DJANGO_SETTINGS_MODULE"] = "BrainQuest.settings"

import django

django.setup()

from restapi.models import ProblemTopics


def insert_topics_data():
    states = ProblemTopics.TOPIC_CHOICES

    for state in states:
        ProblemTopics.objects.create(topic=state[0])


if __name__ == "__main__":
    insert_topics_data()
