# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0003_perfil_contato'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='contato',
        ),
        migrations.AddField(
            model_name='perfil',
            name='contatos',
            field=models.ManyToManyField(related_name='contatos_rel_+', to='perfis.Perfil'),
            preserve_default=True,
        ),
    ]
