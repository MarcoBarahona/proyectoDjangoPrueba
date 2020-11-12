from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect
from django.conf import settings
from nombreAplicacion.models import Producto


# Create your views here.
def plantilla(request):
    return render(request, 'plantillaEjemplo.html' , {})

def login(request):
    mensaje=""
    if request.method == "POST":
        correo    = request.POST["txtCorreo"]
        clave    = request.POST["txtClave"]

        try:
            validate_email(correo)
        except ValidationError as e:
            mensaje = "Porfavor Ingrese un correo válido"
        else:
            User.objects.create( email=correo, password=make_password(clave))
            return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, 'login.html', {})

def cotizaciones(request):
    mensaje=""
    if request.method == "POST":
        nombre     = request.POST["txtNombre"]
        email   = request.POST["txtEmail"]
        telefono = request.POST["txtTelefono"]
        ciudad = request.POST["txtCiudad"]
        producto = request.POST["txtProducto"]
        cantidad = request.POST["txtCantidad"]
        comentario = request.POST["txtComentario"]

        try:
            validate_email(email)
        except ValidationError as e:
            mensaje = "Porfavor Ingrese un email válido"
        else:
            User.objects.create(first_name=nombre, email=email, telefono=telefono, ciudad=ciudad, producto=producto, 
            cantidad=cantidad, comentario=comentario)
            return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, 'cotizaciones.html', {})

def producto(request):
    mensaje=""
    lista={}
    item={}

    if request.method == "POST":
        id      = int("0" + request.POST["txtId"])
        nombre  = request.POST["txtNombre"]
        activo  = request.POST.get("chkActivo") is "1"

        if 'btnGrabar' in request.POST:
            if id < 1:
                producto.objects.create(nombre=nombre, activo=activo)
            else:
                item = producto.objects.get(pk = id)
                item.nombre = nombre
                item.activo = activo
                item.save()
                item = {}
                mensaje= "Datos Guardados Correctamente"
        elif 'btnBuscar' in request.POST:
            item = producto.objects.get(pk = id)

            if not isinstance(item, Producto):
                mensaje = "Registro no encontrado"
                item = {}

        elif 'btnListar' in request.POST:
            lista = producto.objects.all()

        elif 'btnEliminar' in request.POST:
            item = producto.objects.get(pk = id)

            if isinstance(item, producto):
                item.delete()
                mensaje = "Registro eliminado"
                item = {}

    contexto = {'mensaje':mensaje, 'lista' : lista, 'item':item}
    return render(request, 'Producto.html', contexto)