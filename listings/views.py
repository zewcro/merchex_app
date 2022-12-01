from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band
from listings.forms import BandForm, ContactUsForm
from django.core.mail import send_mail
from django.shortcuts import redirect


def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})


def band_detail(request, id):
    # we ask to return the 'band' object with the submited id from url
    band = Band.objects.get(id=id)
    # passage de l'id au model
    return render(request, 'listings/band_detail.html', {'band': band})


def contact(request):
    if request.method == 'POST':
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
        form = ContactUsForm()
        return redirect('email-sent')
    # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
    # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).
    else:
        # ceci doit être une requête GET, donc créer un formulaire vide
        form = ContactUsForm()

        return render(request,
                      'listings/contact.html',
                      {'form': form})


def email_sent(request):
    return render(request, 'listings/email_sent.html')


def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            # créer un nouvel objet bands et l'ajoute dans la base de données
            band = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('band-detail', band.id)

    else:
        # retourne un formulaire vierge
        form = BandForm()
        # retourne le template html
    return render(request,
            'listings/band_create.html',{'form': form})
    
    
def band_update(request, id):
    # on créer un nouvel object 'band' depuis la bdd a partir du model de class et l'id  
    band = Band.objects.get(id=id)

    # si la request est de type 'POST'
    if request.method == 'POST':
        # le formulaire sera celui de la class Bandform est sera pré-rempli avec les donné de l'instance 'band' créer plus tot 
        form = BandForm(request.POST, instance=band)
        # si le formulaire est valide
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('band-detail', band.id)
    else:
        # on re-affiche le formulaire avec les même donnée (comme si non modifiées)
        form = BandForm(instance=band)
        # on retourne notre template html band_update.html
    return render(request, 'listings/band_update.html', {'form': form})



def band_delete(request, id): 
    band = Band.objects.get(id=id)
    
    if request.method == 'POST':
        # on supprime le groupe de la base de données 
        band.delete()
        # et on redirige vers la liste des groupes
        return redirect('band-list')
    return render(request, 'listings/band_delete.html', {'band': band}) 