 
# Generated by Django 1.10.8 on 2017-10-03 21:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutorialv2', '0021_picklistoperation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentreaction',
            name='related_content',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_content_note', to='tutorialv2.PublishableContent', verbose_name='Contenu'),
        ),
        migrations.AlterField(
            model_name='publishablecontent',
            name='authors',
            field=models.ManyToManyField(db_index=True, to=settings.AUTH_USER_MODEL, verbose_name='Auteurs'),
        ),
        migrations.AlterField(
            model_name='publishablecontent',
            name='beta_topic',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='forum.Topic', verbose_name='Sujet beta associé'),
        ),
        migrations.AlterField(
            model_name='publishablecontent',
            name='creation_date',
            field=models.DateTimeField(verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='publishablecontent',
            name='description',
            field=models.CharField(max_length=200, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='publishablecontent',
            name='gallery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gallery.Gallery', verbose_name="Galerie d'images"),
        ),
        migrations.AlterField(
            model_name='publishablecontent',
            name='helps',
            field=models.ManyToManyField(blank=True, db_index=True, to='utils.HelpWriting', verbose_name='Aides'),
        ),
        migrations.AlterField(
            model_name='publishablecontent',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gallery.Image', verbose_name='Image du tutoriel'),
        ),
        migrations.AlterField(
            model_name='publishablecontent',
            name='is_locked',
            field=models.BooleanField(default=False, verbose_name='Est verrouillé'),
        ),
        migrations.AlterField(
            model_name='publishablecontent',
            name='js_support',
            field=models.BooleanField(default=False, verbose_name='Support du Javascript'),
        ),
        migrations.AlterField(
            model_name='publishablecontent',
            name='last_note',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='last_note', to='tutorialv2.ContentReaction', verbose_name='Derniere note'),
        ),
        migrations.AlterField(
            model_name='publishablecontent',
            name='licence',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='utils.Licence', verbose_name='Licence'),
        ),
        migrations.AlterField(
            model_name='publishablecontent',
            name='pubdate',
            field=models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Date de publication'),
        ),
        migrations.AlterField(
            model_name='publishablecontent',
            name='public_version',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tutorialv2.PublishedContent', verbose_name='Version publiée'),
        ),
        migrations.AlterField(
            model_name='publishablecontent',
            name='relative_images_path',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='chemin relatif images'),
        ),
        migrations.AlterField(
            model_name='publishablecontent',
            name='sha_beta',
            field=models.CharField(blank=True, db_index=True, max_length=80, null=True, verbose_name='Sha1 de la version beta publique'),
        ),
        migrations.AlterField(
            model_name='publishablecontent',
            name='sha_draft',
            field=models.CharField(blank=True, db_index=True, max_length=80, null=True, verbose_name='Sha1 de la version de rédaction'),
        ),
        migrations.AlterField(
            model_name='publishablecontent',
            name='sha_public',
            field=models.CharField(blank=True, db_index=True, max_length=80, null=True, verbose_name='Sha1 de la version publique'),
        ),
        migrations.AlterField(
            model_name='publishablecontent',
            name='sha_validation',
            field=models.CharField(blank=True, db_index=True, max_length=80, null=True, verbose_name='Sha1 de la version en validation'),
        ),
        migrations.AlterField(
            model_name='publishablecontent',
            name='slug',
            field=models.CharField(max_length=80, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='publishablecontent',
            name='source',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Source'),
        ),
        migrations.AlterField(
            model_name='publishablecontent',
            name='subcategory',
            field=models.ManyToManyField(blank=True, db_index=True, to='utils.SubCategory', verbose_name='Sous-Catégorie'),
        ),
        migrations.AlterField(
            model_name='publishablecontent',
            name='tags',
            field=models.ManyToManyField(blank=True, db_index=True, to='utils.Tag', verbose_name='Tags du contenu'),
        ),
        migrations.AlterField(
            model_name='publishablecontent',
            name='title',
            field=models.CharField(max_length=80, verbose_name='Titre'),
        ),
        migrations.AlterField(
            model_name='publishablecontent',
            name='type',
            field=models.CharField(choices=[('TUTORIAL', 'Tutoriel'), ('ARTICLE', 'Article'), ('OPINION', 'Billet')], db_index=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='publishablecontent',
            name='update_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date de mise à jour'),
        ),
        migrations.AlterField(
            model_name='publishedcontent',
            name='authors',
            field=models.ManyToManyField(db_index=True, to=settings.AUTH_USER_MODEL, verbose_name='Auteurs'),
        ),
        migrations.AlterField(
            model_name='publishedcontent',
            name='content',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutorialv2.PublishableContent', verbose_name='Contenu'),
        ),
        migrations.AlterField(
            model_name='publishedcontent',
            name='content_pk',
            field=models.IntegerField(db_index=True, verbose_name='Pk du contenu publié'),
        ),
        migrations.AlterField(
            model_name='publishedcontent',
            name='content_public_slug',
            field=models.CharField(max_length=80, verbose_name='Slug du contenu publié'),
        ),
        migrations.AlterField(
            model_name='publishedcontent',
            name='content_type',
            field=models.CharField(choices=[('TUTORIAL', 'Tutoriel'), ('ARTICLE', 'Article'), ('OPINION', 'Billet')], db_index=True, max_length=10, verbose_name='Type de contenu'),
        ),
        migrations.AlterField(
            model_name='publishedcontent',
            name='es_already_indexed',
            field=models.BooleanField(db_index=True, default=False, verbose_name='Déjà indexé par ES'),
        ),
        migrations.AlterField(
            model_name='publishedcontent',
            name='es_flagged',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Doit être (ré)indexé par ES'),
        ),
        migrations.AlterField(
            model_name='publishedcontent',
            name='must_redirect',
            field=models.BooleanField(db_index=True, default=False, verbose_name='Redirection vers  une version plus récente'),
        ),
        migrations.AlterField(
            model_name='publishedcontent',
            name='publication_date',
            field=models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Date de publication'),
        ),
        migrations.AlterField(
            model_name='publishedcontent',
            name='sha_public',
            field=models.CharField(blank=True, db_index=True, max_length=80, null=True, verbose_name='Sha1 de la version publiée'),
        ),
        migrations.AlterField(
            model_name='publishedcontent',
            name='sizes',
            field=models.CharField(default='{}', max_length=512, verbose_name='Tailles des fichiers téléchargeables'),
        ),
        migrations.AlterField(
            model_name='publishedcontent',
            name='update_date',
            field=models.DateTimeField(blank=True, db_index=True, default=None, null=True, verbose_name='Date de mise à jour'),
        ),
        migrations.AlterField(
            model_name='validation',
            name='comment_authors',
            field=models.TextField(blank=True, null=True, verbose_name="Commentaire de l'auteur"),
        ),
        migrations.AlterField(
            model_name='validation',
            name='comment_validator',
            field=models.TextField(blank=True, null=True, verbose_name='Commentaire du validateur'),
        ),
        migrations.AlterField(
            model_name='validation',
            name='content',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tutorialv2.PublishableContent', verbose_name='Contenu proposé'),
        ),
        migrations.AlterField(
            model_name='validation',
            name='date_proposition',
            field=models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Date de proposition'),
        ),
        migrations.AlterField(
            model_name='validation',
            name='date_reserve',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date de réservation'),
        ),
        migrations.AlterField(
            model_name='validation',
            name='date_validation',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date de validation'),
        ),
        migrations.AlterField(
            model_name='validation',
            name='status',
            field=models.CharField(choices=[('PENDING', "En attente d'un validateur"), ('PENDING_V', 'En cours de validation'), ('ACCEPT', 'Publié'), ('REJECT', 'Rejeté'), ('CANCEL', 'Annulé')], default='PENDING', max_length=10),
        ),
        migrations.AlterField(
            model_name='validation',
            name='validator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author_content_validations', to=settings.AUTH_USER_MODEL, verbose_name='Validateur'),
        ),
        migrations.AlterField(
            model_name='validation',
            name='version',
            field=models.CharField(blank=True, db_index=True, max_length=80, null=True, verbose_name='Sha1 de la version'),
        ),
    ]