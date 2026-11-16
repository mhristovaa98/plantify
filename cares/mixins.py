from cares.models import CareLog


class CareStatisticsMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        watering = CareLog.objects.filter(
            care_type=CareLog.CareTypeChoices.WATERING
        ).count()

        fertilizing = CareLog.objects.filter(
            care_type=CareLog.CareTypeChoices.FERTILIZING
        ).count()

        pruning = CareLog.objects.filter(
            care_type=CareLog.CareTypeChoices.PRUNING
        ).count()

        repotting = CareLog.objects.filter(
            care_type=CareLog.CareTypeChoices.REPOTTING
        ).count()

        context['watering_count'] = watering
        context['fertilizing_count'] = fertilizing
        context['pruning_count'] = pruning
        context['repotting_count'] = repotting

        return context