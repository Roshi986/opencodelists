import csv
from io import StringIO

from django.core.management import BaseCommand
from django.db import transaction

from mappings.ctv3sctmap2.mappers import ctv3_to_snomedct

from ...models import Codelist


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("project")
        parser.add_argument("slug")

    def handle(self, project, slug, **kwargs):
        convert_codelist(project, slug)


def convert_codelist(project, slug):
    codelist = Codelist.objects.get(project_id=project, slug=slug)
    assert codelist.coding_system_id in ["ctv3", "ctv3tpp"]

    version = codelist.versions.first()

    buf = StringIO()
    writer = csv.writer(buf)
    writer.writerow(["id", "name", "active", "notes"])
    for record in ctv3_to_snomedct(version.codes):
        writer.writerow(
            [
                record["id"],
                record["name"],
                "y" if record["active"] else "n",
                record["notes"],
            ]
        )

    with transaction.atomic():
        codelist = Codelist.objects.create(
            name=codelist.name + " (SNOMED)",
            project=codelist.project,
            coding_system_id="snomedct",
            description=f"Automatically-generated equivalent of [{codelist.name}]({codelist.get_absolute_url()})",
            methodology="See [code on GitHub](https://github.com/opensafely/opencodelists/blob/master/codelists/management/commands/convert_codelist.py)",
        )

        codelist.versions.create(
            version_str=version.version_str,
            csv_data=buf.getvalue(),
        )
