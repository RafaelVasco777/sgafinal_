from django.shortcuts import render, redirect, get_object_or_404
from .models import Imovel, Proprietario, Cliente, Contrato, Pagamento, Corretor, Imobiliaria
from .forms import ImovelForm, ProprietarioForm, ClienteForm, ContratoForm, PagamentoForm, CorretorForm, ImobiliariaForm
from django.shortcuts import render


def imovel_list(request):
    imoveis = Imovel.objects.all()
    return render(request, 'core/imovel_list.html', {'imoveis': imoveis})

def imovel_create(request):
    if request.method == "POST":
        form = ImovelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('imovel_list')
    else:
        form = ImovelForm()
    return render(request, 'core/imovel_form.html', {'form': form})

def imovel_update(request, pk):
    imovel = get_object_or_404(Imovel, pk=pk)
    if request.method == "POST":
        form = ImovelForm(request.POST, request.FILES, instance=imovel)
        if form.is_valid():
            form.save()
            return redirect('imovel_list')
    else:
        form = ImovelForm(instance=imovel)
    return render(request, 'core/imovel_form.html', {'form': form})

def imovel_delete(request, pk):
    imovel = get_object_or_404(Imovel, pk=pk)
    if request.method == "POST":
        imovel.delete()
        return redirect('imovel_list')
    return render(request, 'core/imovel_confirm_delete.html', {'imovel': imovel})

def proprietario_list(request):
    proprietarios = Proprietario.objects.all()
    return render(request, 'core/proprietario_list.html', {'proprietarios': proprietarios})

def proprietario_create(request):
    if request.method == "POST":
        form = ProprietarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proprietario_list')
    else:
        form = ProprietarioForm()
    return render(request, 'core/proprietario_form.html', {'form': form})

def proprietario_update(request, pk):
    proprietario = get_object_or_404(Proprietario, pk=pk)
    if request.method == "POST":
        form = ProprietarioForm(request.POST, instance=proprietario)
        if form.is_valid():
            form.save()
            return redirect('proprietario_list')
    else:
        form = ProprietarioForm(instance=proprietario)
    return render(request, 'core/proprietario_form.html', {'form': form})

def proprietario_delete(request, pk):
    proprietario = get_object_or_404(Proprietario, pk=pk)
    if request.method == "POST":
        proprietario.delete()
        return redirect('proprietario_list')
    return render(request, 'core/proprietario_confirm_delete.html', {'proprietario': proprietario})

def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'core/cliente_list.html', {'clientes': clientes})

def cliente_create(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm()
    return render(request, 'core/cliente_form.html', {'form': form})

def cliente_update(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'core/cliente_form.html', {'form': form})

def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        cliente.delete()
        return redirect('cliente_list')
    return render(request, 'core/cliente_confirm_delete.html', {'cliente': cliente})

def contrato_list(request):
    contratos = Contrato.objects.all()
    return render(request, 'core/contrato_list.html', {'contratos': contratos})

def contrato_create(request):
    if request.method == "POST":
        form = ContratoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contrato_list')
    else:
        form = ContratoForm()
    return render(request, 'core/contrato_form.html', {'form': form})

def contrato_update(request, pk):
    contrato = get_object_or_404(Contrato, pk=pk)
    if request.method == "POST":
        form = ContratoForm(request.POST, instance=contrato)
        if form.is_valid():
            form.save()
            return redirect('contrato_list')
    else:
        form = ContratoForm(instance=contrato)
    return render(request, 'core/contrato_form.html', {'form': form})

def contrato_delete(request, pk):
    contrato = get_object_or_404(Contrato, pk=pk)
    if request.method == "POST":
        contrato.delete()
        return redirect('contrato_list')
    return render(request, 'core/contrato_confirm_delete.html', {'contrato': contrato})

def pagamento_list(request):
    pagamentos = Pagamento.objects.all()
    return render(request, 'core/pagamento_list.html', {'pagamentos': pagamentos})

def pagamento_create(request):
    if request.method == "POST":
        form = PagamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagamento_list')
    else:
        form = PagamentoForm()
    return render(request, 'core/pagamento_form.html', {'form': form})

def pagamento_update(request, pk):
    pagamento = get_object_or_404(Pagamento, pk=pk)
    if request.method == "POST":
        form = PagamentoForm(request.POST, instance=pagamento)
        if form.is_valid():
            form.save()
            return redirect('pagamento_list')
    else:
        form = PagamentoForm(instance=pagamento)
    return render(request, 'core/pagamento_form.html', {'form': form})

def pagamento_delete(request, pk):
    pagamento = get_object_or_404(Pagamento, pk=pk)
    if request.method == "POST":
        pagamento.delete()
        return redirect('pagamento_list')
    return render(request, 'core/pagamento_confirm_delete.html', {'pagamento': pagamento})

def corretor_list(request):
    corretores = Corretor.objects.all()
    return render(request, 'core/corretor_list.html', {'corretores': corretores})

def corretor_create(request):
    if request.method == "POST":
        form = CorretorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('corretor_list')
    else:
        form = CorretorForm()
    return render(request, 'core/corretor_form.html', {'form': form})

def corretor_update(request, pk):
    corretor = get_object_or_404(Corretor, pk=pk)
    if request.method == "POST":
        form = CorretorForm(request.POST, instance=corretor)
        if form.is_valid():
            form.save()
            return redirect('corretor_list')
    else:
        form = CorretorForm(instance=corretor)
    return render(request, 'core/corretor_form.html', {'form': form})

def corretor_delete(request, pk):
    corretor = get_object_or_404(Corretor, pk=pk)
    if request.method == "POST":
        corretor.delete()
        return redirect('corretor_list')
    return render(request, 'core/corretor_confirm_delete.html', {'corretor': corretor})

def imobiliaria_list(request):
    imobiliarias = Imobiliaria.objects.all()
    return render(request, 'core/imobiliaria_list.html', {'imobiliarias': imobiliarias})

def imobiliaria_create(request):
    if request.method == "POST":
        form = ImobiliariaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('imobiliaria_list')
    else:
        form = ImobiliariaForm()
    return render(request, 'core/imobiliaria_form.html', {'form': form})

def imobiliaria_update(request, pk):
    imobiliaria = get_object_or_404(Imobiliaria, pk=pk)
    if request.method == "POST":
        form = ImobiliariaForm(request.POST, instance=imobiliaria)
        if form.is_valid():
            form.save()
            return redirect('imobiliaria_list')
    else:
        form = ImobiliariaForm(instance=imobiliaria)
    return render(request, 'core/imobiliaria_form.html', {'form': form})

def imobiliaria_delete(request, pk):
    imobiliaria = get_object_or_404(Imobiliaria, pk=pk)
    if request.method == "POST":
        imobiliaria.delete()
        return redirect('imobiliaria_list')
    return render(request, 'core/imobiliaria_confirm_delete.html', {'imobiliaria': imobiliaria})

def index(request):
    return render(request, 'core/index.html')