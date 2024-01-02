import tkinter as tk
from tkinter import messagebox
import os

def adicionar_tarefa():
    tarefa = entrada_tarefa.get()
    if tarefa:
        lista_tarefas.insert(tk.END, tarefa)
        entrada_tarefa.delete(0, tk.END)
        salvar_tarefas()
    else:
        messagebox.showwarning("Aviso", "Por favor, insira uma tarefa.")

def marcar_concluida():
    try:
        selecao = lista_tarefas.curselection()
        indice = selecao[0]
        lista_tarefas.itemconfig(indice, {'bg': 'light blue', 'fg': 'gray'})
        salvar_tarefas()
    except IndexError:
        pass

def excluir_tarefa():
    try:
        selecao = lista_tarefas.curselection()
        indice = selecao[0]
        lista_tarefas.delete(indice)
        salvar_tarefas()
    except IndexError:
        pass

def salvar_tarefas():
    with open('tarefas.txt', 'w') as arquivo:
        tarefas = lista_tarefas.get(0, tk.END)
        for tarefa in tarefas:
            arquivo.write(tarefa + '\n')

def carregar_tarefas():
    if os.path.exists('tarefas.txt'):
        with open('tarefas.txt', 'r') as arquivo:
            for linha in arquivo:
                lista_tarefas.insert(tk.END, linha.strip())

janela = tk.Tk()
janela.title("Lista de Tarefas")

entrada_tarefa = tk.Entry(janela, width=15)
entrada_tarefa.pack(pady=15)

botao_adicionar = tk.Button(janela, text="Adicionar Tarefa", command=adicionar_tarefa)
botao_adicionar.pack()

lista_tarefas = tk.Listbox(janela, selectbackground="blue", selectmode=tk.SINGLE)
lista_tarefas.pack(padx=15, pady=15)

botao_concluir = tk.Button(janela, text="Marcar Concluída", command=marcar_concluida)
botao_concluir.pack()

botao_excluir = tk.Button(janela, text="Excluir Tarefa", command=excluir_tarefa)
botao_excluir.pack()

carregar_tarefas()

janela.mainloop()
