from logging import root
import self as self
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.factory import FactoryException
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.card import MDCard
from kivymd.uix.toolbar.toolbar import ActionTopAppBarButton
from kivymd.uix.toolbar.toolbar import MDTopAppBar
from kivy.properties import StringProperty
from kivymd.uix.label import MDLabel
from kivymd.font_definitions import theme_font_styles
from kivymd.uix.label.label import NumericProperty
from kivymd.uix.label.label import MDIcon
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.navigationdrawer import MDNavigationDrawer, MDNavigationDrawerItem, MDNavigationDrawerLabel
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine
import os
from kivymd import images_path
from kivymd.uix.list.list import IconLeftWidget
from kivymd.uix.list import IRightBodyTouch, ThreeLineListItem, OneLineAvatarIconListItem
from kivy.properties import Property
from kivy.uix.textinput import TextInput
import requests
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty
from kivymd.icon_definitions import md_icons
from kivymd.uix.selectioncontrol import MDCheckbox
from data import data as ListItems
from kivymd.uix.list import ThreeLineAvatarIconListItem


Window.size = (500, 900)


class TelaCriarConta(Screen):
    pass


class TelaRecSenha(Screen):
    pass


class TelaLogin(Screen):
    pass


class TelaHome(Screen):
    pass

class DrawerLabelItem(MDNavigationDrawerItem):
    pass


class DrawerClickableItem(MDNavigationDrawerItem):
    pass


class TelaEnd(Screen):
    def END(self):
        for it in ListItems:
            _it = ThreeLineAvatarIconListItem(
                text=it["texto"],
                secondary_text=it["secondary_text"],
                tertiary_text=it["tertiary_text"]
            )
            _it.add_widget(MDIcon)(
                icon=it["IconLeft"]
            )
            (
                _it.add_widget(MDIcon)(
                    icon=it["IconRight"]
                )
            )
        self.root.ids.lista.add_widget(_it)


class TelaCriarEnd(Screen):
    pass


class BuscaCEP(Screen):
    pass


class BuscaEnd(Screen):
    def CEP(self):
        cep1 = 0
        cep1 = self.ids.cep1.text
        if len(cep1) == 8:
            link = f"https://viacep.com.br/ws/{cep1}/json/"
            requisicao = requests.get(link)
            if requisicao.json() != {'erro': True}:
                self.ids.cepin.text = f'CEP: {requisicao.json()["cep"]}'
                self.ids.logradouro.text = f'RUA: {requisicao.json()["logradouro"]}'
                self.ids.complemento.text = f'COMPLEMENTO: {requisicao.json()["complemento"]}'
                self.ids.bairro.text = f'BAIRRO: {requisicao.json()["bairro"]}'
                self.ids.localidade.text = f'CIDADE: {requisicao.json()["localidade"]}'
                self.ids.uf.text = f'UF: {requisicao.json()["uf"]}'
                self.ids.ddd.text = f'DDD: {requisicao.json()["ddd"]}'
            else:
                self.ids.cepin.text = "CEP NÃO ENCONTRADO!"
        else:
            self.ids.cepin.text = "CEP INVALIDO!"






class main(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Blue'

        sm = ScreenManager()
        sm.add_widget(TelaLogin(name="TelaLogin"))
        sm.add_widget(TelaHome(name="TelaHome"))
        sm.add_widget(TelaEnd(name="TelaEnd"))
        sm.add_widget(TelaRecSenha(name="TelaRecSenha"))
        sm.add_widget(TelaCriarConta(name="TelaCriarConta"))
        sm.add_widget(TelaCriarEnd(name="TelaCriarEnd"))
        sm.add_widget(BuscaCEP(name="BuscaCEP"))
        sm.add_widget(BuscaEnd(name="BuscaEnd"))



        return sm



main().run()
