from django.db import models

# Create your models here.


class Alumno(models.Model):
    id_a = models.FloatField(primary_key=True)
    nom = models.CharField(max_length=45)
    edad = models.IntegerField()
    id_curso2 = models.ForeignKey('Curso', models.DO_NOTHING, db_column='id_curso2')
    matricula_cod_mat = models.OneToOneField('Matricula', models.DO_NOTHING, db_column='matricula_cod_mat')

    class Meta:
        managed = False
        db_table = 'alumno'


class Asignatura(models.Model):
    id_asig = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'asignatura'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Curso(models.Model):
    id_curso = models.FloatField(primary_key=True)
    grado_curso = models.CharField(max_length=15)
    num_aula = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'curso'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class HorarioDetalle(models.Model):
    hora_ini = models.TimeField()
    hora_fin = models.TimeField()
    dia = models.CharField(max_length=10)
    id_curso1 = models.ForeignKey(Curso, models.DO_NOTHING, db_column='id_curso1')
    id_asig1 = models.ForeignKey(Asignatura, models.DO_NOTHING, db_column='id_asig1')
    cod_h = models.FloatField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'horario_detalle'


class Matricula(models.Model):
    cod_mat = models.AutoField(primary_key=True)
    fecha_mat = models.DateField()
    costo = models.FloatField()

    class Meta:
        managed = False
        db_table = 'matricula'


class ProfCurso(models.Model):
    id_curso3 = models.ForeignKey(Curso, models.DO_NOTHING, db_column='id_curso3')
    id_profe2 = models.ForeignKey('Profesor', models.DO_NOTHING, db_column='id_profe2')
    cod = models.FloatField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'prof_curso'


class Profesor(models.Model):
    id_profe = models.FloatField(primary_key=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    profesion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'profesor'