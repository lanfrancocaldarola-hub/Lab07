import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
- Funziona da intermediario tra MODELLO e VIEW

- Gestisce la logica del flusso dell'applicazione

'''


class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    def popola_dropdown(self):
        biblioteche = self._model.get_biblioteche()
        self._view.dd_biblioteca.options.append(ft.dropdown.Option(key="NONE", text="Nessun filtro"))
        for b in biblioteche:
            self._view.dd_biblioteca.options.append(ft.dropdown.Option(key=str(b.id), text=b.nome))

        generi = self._model.get_generi()
        self._view.dd_genere.options.append(ft.dropdown.Option(key="NONE", text="Nessun filtro"))
        for g in generi:
            self._view.dd_genere.options.append(ft.dropdown.Option(key=g, text=g))

    def leggi_biblioteca(self, e):
        valore = self._view.dd_biblioteca.value
        if valore == "NONE" or valore is None:
            self.biblioteca_selezionata = None
        else:
            self.biblioteca_selezionata = valore

    def leggi_genere(self, e):
        valore = self._view.dd_genere.value
        if valore == "NONE" or valore is None:
            self.genere_selezionato = None
        else:
            self.genere_selezionato = valore

    def handle_mostra_libri(self, e):
        self._view.lst_libri.controls.clear()

        libri = self._model.get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato)

        if not libri:
            self._view.show_alert("Nessun libro trovato con i criteri selezionati.")
            self._view.update()
            return

        for libro in libri:
            testo = f"{libro.titolo} - {libro.autore} ({libro.genere})"
            self._view.lst_libri.controls.append(ft.Text(testo))

        self._view.update()