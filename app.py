import customtkinter as ctk
import tkinter.ttk as ttk
from tkinter import messagebox 

# Configuração de aparência
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme("dark-blue")

class LoginApp:
    def __init__(self):
        self.login_window = ctk.CTk()
        self.login_window.title("Sistema de Login")
        self.login_window.geometry("500x300")
        
        self.criar_interface_login()

    def criar_interface_login(self):
        """Cria a interface de login"""
        frame = ctk.CTkFrame(self.login_window)
        frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        # Título
        ctk.CTkLabel(frame, text="Fazer Login", font=ctk.CTkFont(size=18, weight="bold")).pack(pady=12)
        
        # Campos de entrada
        self.campo_usuario = ctk.CTkEntry(frame, placeholder_text="Digite seu usuário")
        self.campo_usuario.pack(pady=5, padx=10)
        
        self.campo_senha = ctk.CTkEntry(frame, placeholder_text="Digite sua senha", show="*")
        self.campo_senha.pack(pady=5, padx=10)
        
        checkbox = ctk.CTkCheckBox(frame, text="Lembrar Login")
        checkbox.pack(pady=5)
        
        # Botão de login
        ctk.CTkButton(
            frame, 
            text="Login", 
            command=self.validar_login,
            fg_color="#4CAF50",
            hover_color="#388E3C"
        ).pack(pady=12, padx=10)
        
        # Feedback
        self.resultado_login = ctk.CTkLabel(frame, text="")
        self.resultado_login.pack(pady=5)
    
    def validar_login(self):
        """Valida as credenciais de login"""
        usuario = self.campo_usuario.get()
        senha = self.campo_senha.get()
        
        if usuario == 'admin' and senha == '1234':
            self.resultado_login.configure(text="Login realizado com sucesso!", text_color="green")
            self.login_window.after(1000, self.iniciar_sistema_pizzaria)
        else:
            self.resultado_login.configure(text="Usuário ou senha incorretos!", text_color="red")
    
    def iniciar_sistema_pizzaria(self):
        """Inicia o sistema principal após login"""
        self.login_window.withdraw()  # Esconde a janela de login
        PizzariaApp(self.login_window)  # Passa a referência da janela de login

class PizzariaApp(ctk.CTkToplevel):
    def __init__(self, login_window):
        super().__init__()
        self.login_window = login_window
        
        # Configuração da janela principal
        self.title("Manollos Pizzaria - Sistema de Pedidos")
        self.geometry("1200x800")
        self.minsize(1000, 700)
        
        # Protocolo para quando a janela for fechada
        self.protocol("WM_DELETE_WINDOW", self.voltar_ao_login)
        
        # Inicialização de dados
        self.inicializar_dados()
        
        # Criar interface
        self.criar_interface()
    
    def voltar_ao_login(self):
        """Volta para a tela de login quando fechar o sistema"""
        self.destroy()
        self.login_window.deiconify()
    
    def inicializar_dados(self):
        """Inicializa os dados da pizzaria"""
        self.pizzas = [
            {"id": 1, "nome": "Portuguesa", "preco": 30.00, "ingredientes": "Presunto, queijo, ovo, cebola, azeitona"},
            {"id": 2, "nome": "Marguerita", "preco": 35.00, "ingredientes": "Queijo, tomate, manjericão"},
            {"id": 3, "nome": "Frango com Catupiry", "preco": 40.00, "ingredientes": "Frango desfiado, catupiry"},
            {"id": 4, "nome": "Calabresa", "preco": 32.00, "ingredientes": "Calabresa, cebola"},
            {"id": 5, "nome": 'Quatro Queijos', 'preco': 37.00, "ingredientes": "Queijo muçarela, queijo gorgonzola, queijo parmesão, queijo catupiry"},
            {"id": 6, "nome": 'Alho e óleo', 'preco': 42.00,  "ingredientes": "Alho, azeite, queijo"},
            {"id": 7, "nome": 'Vegetariana', 'preco': 34.00,"ingredientes": "Brócolis, cenoura, pimentão, cebola"},
            {"id": 8, "nome": "Pepperoni", "preco": 38.00, "ingredientes": "Pepperoni, queijo, molho de tomate"},
            {"id": 9, "nome": "Napolitana", "preco": 36.00, "ingredientes": "Tomate, queijo, manjericão, alho"},
            {"id": 10, "nome": "Bacon", "preco": 39.00, "ingredientes": "Bacon, queijo, cebola"},
            {"id": 11, "nome": "Atum", "preco": 37.00, "ingredientes": "Atum, cebola, azeitonas"},
            {"id": 12, "nome": "Mexicana", "preco": 41.00, "ingredientes": "Carne moída, pimentão, pimenta"}
        ]
        
        self.bordas = [
            {"id": 0, "nome": "Sem borda", "preco": 0.00},
            {"id": 1, "nome": "Borda de Catupiry", "preco": 5.00},
            {"id": 2, "nome": "Borda de Cheddar", "preco": 6.00},
            {"id": 4, "nome": "Borda de Doce de leite", "preco": 8.50},
            {"id": 5, "nome": "Borda Romeu e Julieta", "preco": 10.50},
            {"id": 6, "nome": "Borda de Leite Ninho", "preco": 9.50}
        ]
        
        self.bebidas = [
            {"id": 1, "nome": "Coca-Cola", "preco": 8.00, "tamanho": "350ml"},
            {"id": 2, "nome": "Guaraná", "preco": 7.00, "tamanho": "350ml"},
            {"id": 3, "nome": "Água", "preco": 4.00, "tamanho": "500ml"},
            {"id": 4, "nome": "Suco natural de Maracujá", "preco": 15.00, "tamanho": "500ml"},
            {"id": 5, "nome": "Suco natural de Laranja", "preco": 10.00, "tamanho": "500ml"},
            {"id": 6, "nome": "Suco natural de Goiaba", "preco": 13.00, "tamanho": "500ml"},
            {"id": 7, "nome": "Cerveja", "preco": 12.00, "tamanho": "600ml"},
            {"id": 8, "nome": "Refrigerante Lata", "preco": 6.00, "tamanho": "350ml"},
            {"id": 9, "nome": "Água com Gás", "preco": 5.00, "tamanho": "500ml"},
            {"id": 10, "nome": "Energético", "preco": 14.00, "tamanho": "250ml"}
        ]
        
        self.fila_pedidos = []
        self.contador_pedidos = 1
        self.pedido_atual = None
    
    def criar_interface(self):
        """Cria toda a interface gráfica"""
        # Configuração do grid principal
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # Criar o notebook (abas)
        self.notebook = ctk.CTkTabview(self)
        self.notebook.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
        # Adicionar abas
        self.notebook.add("Cardápio")
        self.notebook.add("Novo Pedido")
        self.notebook.add("Fila de Pedidos")
        
        # Configurar cada aba
        self.criar_aba_cardapio()
        self.criar_aba_pedido()
        self.criar_aba_fila()
        
        # Inicializar um novo pedido
        self.novo_pedido()
    
    def criar_aba_cardapio(self):
        """Cria a aba de cardápio"""
        aba = self.notebook.tab("Cardápio")
        
        # Notebook interno para categorias
        tabview = ctk.CTkTabview(aba)
        tabview.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Aba de Pizzas
        tabview.add("Pizzas")
        self.criar_tabela_cardapio(tabview.tab("Pizzas"), self.pizzas, "Pizzas")
        
        # Aba de Bordas
        tabview.add("Bordas")
        self.criar_tabela_cardapio(tabview.tab("Bordas"), self.bordas, "Bordas")
        
        # Aba de Bebidas
        tabview.add("Bebidas")
        self.criar_tabela_cardapio(tabview.tab("Bebidas"), self.bebidas, "Bebidas")
    
    def criar_tabela_cardapio(self, frame, dados, titulo):
        """Cria uma tabela de cardápio"""
        # Frame de cabeçalho
        header_frame = ctk.CTkFrame(frame, fg_color="transparent")
        header_frame.pack(fill="x", padx=5, pady=5)
        
        # Título
        ctk.CTkLabel(header_frame, text=titulo, font=ctk.CTkFont(size=16, weight="bold")).pack(side="left")
        
        # Frame da tabela
        table_frame = ctk.CTkFrame(frame)
        table_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Treeview
        style = ttk.Style()
        style.configure("Cardapio.Treeview", rowheight=30, font=('Segoe UI', 10))
        style.configure("Cardapio.Treeview.Heading", font=('Segoe UI', 10, 'bold'))
        
        tree = ttk.Treeview(
            table_frame,
            columns=("id", "nome", "preco", "detalhes"),
            show="headings",
            style="Cardapio.Treeview"
        )
        
        # Configurar colunas
        tree.heading("id", text="Código")
        tree.heading("nome", text="Item")
        tree.heading("preco", text="Preço (R$)")
        tree.heading("detalhes", text="Detalhes")
        
        tree.column("id", width=80, anchor="center")
        tree.column("nome", width=200)
        tree.column("preco", width=100, anchor="center")
        tree.column("detalhes", width=300)
        
        # Adicionar itens
        for item in dados:
            detalhes = item.get("ingredientes", item.get("tamanho", ""))
            tree.insert("", "end", values=(item["id"], item["nome"], f"R$ {item['preco']:.2f}", detalhes))
        
        # Barra de rolagem
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        
        # Layout
        tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def criar_aba_pedido(self):
        """Cria a aba de novo pedido"""
        aba = self.notebook.tab("Novo Pedido")
        
        # Configurar grid
        aba.grid_columnconfigure(0, weight=1)
        aba.grid_rowconfigure(0, weight=0)
        aba.grid_rowconfigure(1, weight=0)
        aba.grid_rowconfigure(2, weight=0)
        aba.grid_rowconfigure(3, weight=1)
        aba.grid_rowconfigure(4, weight=0)
        aba.grid_rowconfigure(5, weight=0)
        
        # Frame do cabeçalho
        header_frame = ctk.CTkFrame(aba, fg_color="transparent")
        header_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
        
        ctk.CTkLabel(header_frame, text="Novo Pedido", font=ctk.CTkFont(size=16, weight="bold")).pack(side="left")
        
        # Frame do cliente
        cliente_frame = ctk.CTkFrame(aba, fg_color="transparent")
        cliente_frame.grid(row=1, column=0, sticky="ew", padx=10, pady=5)
        
        ctk.CTkLabel(cliente_frame, text="Nome do Cliente:").pack(anchor="w")
        self.cliente_entry = ctk.CTkEntry(cliente_frame)
        self.cliente_entry.pack(fill="x", pady=5)
        
        # Frame dos botões de ação
        botoes_frame = ctk.CTkFrame(aba, fg_color="transparent")
        botoes_frame.grid(row=2, column=0, sticky="ew", padx=10, pady=5)
        
        # Configurar grid do frame de botões
        botoes_frame.grid_columnconfigure(0, weight=1)
        botoes_frame.grid_columnconfigure(1, weight=1)
        botoes_frame.grid_columnconfigure(2, weight=1)
        
        # Botões centralizados e expandidos
        ctk.CTkButton(
            botoes_frame, 
            text="Adicionar Pizza", 
            command=lambda: self.adicionar_item("pizza"),
            fg_color="#4CAF50",
            hover_color="#388E3C"
        ).grid(row=0, column=0, padx=5, sticky="ew")
        
        ctk.CTkButton(
            botoes_frame, 
            text="Adicionar Borda", 
            command=lambda: self.adicionar_item("borda"),
            fg_color="#2196F3",
            hover_color="#1976D2"
        ).grid(row=0, column=1, padx=5, sticky="ew")
        
        ctk.CTkButton(
            botoes_frame, 
            text="Adicionar Bebida", 
            command=lambda: self.adicionar_item("bebida"),
            fg_color="#00BCD4",
            hover_color="#0097A7"
        ).grid(row=0, column=2, padx=5, sticky="ew")
        
        # Frame dos itens do pedido
        itens_frame = ctk.CTkFrame(aba)
        itens_frame.grid(row=3, column=0, sticky="nsew", padx=10, pady=5)
        itens_frame.grid_columnconfigure(0, weight=1)
        itens_frame.grid_rowconfigure(0, weight=1)
        
        # Treeview dos itens
        style = ttk.Style()
        style.configure("Itens.Treeview", rowheight=30, font=('Segoe UI', 10))
        style.configure("Itens.Treeview.Heading", font=('Segoe UI', 10, 'bold'))
        
        self.tree_itens = ttk.Treeview(
            itens_frame,
            columns=("tipo", "nome", "quantidade", "preco", "subtotal"),
            show="headings",
            style="Itens.Treeview"
        )
        
        # Configurar colunas
        self.tree_itens.heading("tipo", text="Tipo")
        self.tree_itens.heading("nome", text="Item")
        self.tree_itens.heading("quantidade", text="Qtd")
        self.tree_itens.heading("preco", text="Preço Unit.")
        self.tree_itens.heading("subtotal", text="Subtotal")
        
        self.tree_itens.column("tipo", width=80)
        self.tree_itens.column("nome", width=200)
        self.tree_itens.column("quantidade", width=60, anchor="center")
        self.tree_itens.column("preco", width=100, anchor="e")
        self.tree_itens.column("subtotal", width=100, anchor="e")
        
        # Barra de rolagem
        scrollbar = ttk.Scrollbar(itens_frame, orient="vertical", command=self.tree_itens.yview)
        self.tree_itens.configure(yscrollcommand=scrollbar.set)
        
        # Layout
        self.tree_itens.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")
        
        # Frame do total
        total_frame = ctk.CTkFrame(aba, fg_color="transparent")
        total_frame.grid(row=4, column=0, sticky="e", padx=10, pady=5)
        
        ctk.CTkLabel(total_frame, text="Total:", font=ctk.CTkFont(weight="bold")).pack(side="left", padx=5)
        self.total_var = ctk.StringVar(value="R$ 0.00")
        ctk.CTkLabel(total_frame, textvariable=self.total_var, font=ctk.CTkFont(size=14, weight="bold")).pack(side="left")
        
        # Frame dos botões de ação
        acoes_frame = ctk.CTkFrame(aba, fg_color="transparent")
        acoes_frame.grid(row=5, column=0, sticky="e", padx=10, pady=10)
        
        ctk.CTkButton(
            acoes_frame,
            text="Novo Pedido",
            command=self.novo_pedido,
            fg_color="#607D8B",
            hover_color="#455A64"
        ).pack(side="left", padx=5)
        
        ctk.CTkButton(
            acoes_frame,
            text="Finalizar Pedido",
            command=self.finalizar_pedido,
            fg_color="#4CAF50",
            hover_color="#388E3C"
        ).pack(side="left", padx=5)
        
        ctk.CTkButton(
            acoes_frame,
            text="Cancelar",
            command=self.cancelar_pedido,
            fg_color="#F44336",
            hover_color="#D32F2F"
        ).pack(side="left", padx=5)
    
    def criar_aba_fila(self):
        """Cria a aba de fila de pedidos"""
        aba = self.notebook.tab("Fila de Pedidos")
        
        # Configurar grid
        aba.grid_columnconfigure(0, weight=1)
        aba.grid_rowconfigure(0, weight=0)
        aba.grid_rowconfigure(1, weight=1)
        aba.grid_rowconfigure(2, weight=0)
        
        # Frame do cabeçalho
        header_frame = ctk.CTkFrame(aba, fg_color="transparent")
        header_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
        
        ctk.CTkLabel(header_frame, text="Fila de Pedidos", font=ctk.CTkFont(size=16, weight="bold")).pack(side="left")
        
        # Frame da tabela
        table_frame = ctk.CTkFrame(aba)
        table_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)
        table_frame.grid_columnconfigure(0, weight=1)
        table_frame.grid_rowconfigure(0, weight=1)
        
        # Treeview dos pedidos
        style = ttk.Style()
        style.configure("Fila.Treeview", rowheight=30, font=('Segoe UI', 10))
        style.configure("Fila.Treeview.Heading", font=('Segoe UI', 10, 'bold'))
        
        self.tree_pedidos = ttk.Treeview(
            table_frame,
            columns=("numero", "cliente", "total", "itens"),
            show="headings",
            style="Fila.Treeview"
        )
        
        # Configurar colunas
        self.tree_pedidos.heading("numero", text="Nº Pedido")
        self.tree_pedidos.heading("cliente", text="Cliente")
        self.tree_pedidos.heading("total", text="Total (R$)")
        self.tree_pedidos.heading("itens", text="Itens")
        
        self.tree_pedidos.column("numero", width=80, anchor="center")
        self.tree_pedidos.column("cliente", width=150)
        self.tree_pedidos.column("total", width=100, anchor="e")
        self.tree_pedidos.column("itens", width=500)
        
        # Barra de rolagem
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree_pedidos.yview)
        self.tree_pedidos.configure(yscrollcommand=scrollbar.set)
        
        # Layout
        self.tree_pedidos.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")
        
        # Frame dos botões
        botoes_frame = ctk.CTkFrame(aba, fg_color="transparent")
        botoes_frame.grid(row=2, column=0, sticky="e", padx=10, pady=10)
        
        ctk.CTkButton(
            botoes_frame,
            text="Atualizar",
            command=self.atualizar_fila,
            fg_color="#2196F3",
            hover_color="#1976D2"
        ).pack(side="left", padx=5)
        
        ctk.CTkButton(
            botoes_frame,
            text="Entregar Pedido",
            command=self.entregar_pedido,
            fg_color="#4CAF50",
            hover_color="#388E3C"
        ).pack(side="left", padx=5)
    
    def novo_pedido(self):
        """Inicia um novo pedido"""
        self.pedido_atual = {
            "numero": self.contador_pedidos,
            "cliente": "",
            "itens": [],
            "total": 0.0
        }
        self.contador_pedidos += 1
        self.cliente_entry.delete(0, "end")
        self.tree_itens.delete(*self.tree_itens.get_children())
        self.total_var.set("R$ 0.00")
        self.notebook.set("Novo Pedido")
    
    def adicionar_item(self, tipo_item):
        """Abre janela para adicionar item ao pedido"""
        top = ctk.CTkToplevel(self)
        top.title(f"Adicionar {tipo_item.capitalize()}")
        top.geometry("600x500")  # Janela maior
        top.resizable(True, True)  # Permite redimensionamento
        
        # Determinar qual cardápio usar
        if tipo_item == "pizza":
            cardapio = self.pizzas
        elif tipo_item == "borda":
            cardapio = self.bordas
        else:
            cardapio = self.bebidas
        
        # Configurar grid da janela
        top.grid_columnconfigure(0, weight=1)
        top.grid_rowconfigure(0, weight=0)
        top.grid_rowconfigure(1, weight=1)  # Tabela expandível
        top.grid_rowconfigure(2, weight=0)
        top.grid_rowconfigure(3, weight=0)
        
        # Frame do cabeçalho
        header_frame = ctk.CTkFrame(top, fg_color="transparent")
        header_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
        
        ctk.CTkLabel(header_frame, text=f"Selecione {tipo_item}", 
                    font=ctk.CTkFont(size=14, weight="bold")).pack(side="left")
        
        # Frame da tabela
        table_frame = ctk.CTkFrame(top)
        table_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)
        table_frame.grid_columnconfigure(0, weight=1)
        table_frame.grid_rowconfigure(0, weight=1)
        
        # Treeview
        style = ttk.Style()
        style.configure("Selecao.Treeview", rowheight=30, font=('Segoe UI', 10))
        
        tree = ttk.Treeview(
            table_frame,
            columns=("id", "nome", "preco"),
            show="headings",
            style="Selecao.Treeview"
        )
        
        tree.heading("id", text="Código")
        tree.heading("nome", text="Item")
        tree.heading("preco", text="Preço (R$)")
        
        tree.column("id", width=80, anchor="center")
        tree.column("nome", width=250)  # Largura maior
        tree.column("preco", width=100, anchor="e")
        
        for item in cardapio:
            tree.insert("", "end", values=(item["id"], item["nome"], f"R$ {item['preco']:.2f}"))
        
        # Barra de rolagem vertical
        scrollbar_v = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar_v.set)
        
        # Barra de rolagem horizontal
        scrollbar_h = ttk.Scrollbar(table_frame, orient="horizontal", command=tree.xview)
        tree.configure(xscrollcommand=scrollbar_h.set)
        
        # Layout usando grid
        tree.grid(row=0, column=0, sticky="nsew")
        scrollbar_v.grid(row=0, column=1, sticky="ns")
        scrollbar_h.grid(row=1, column=0, sticky="ew")
        
        # Frame da quantidade
        qtd_frame = ctk.CTkFrame(top, fg_color="transparent")
        qtd_frame.grid(row=2, column=0, sticky="ew", padx=10, pady=5)
        
        ctk.CTkLabel(qtd_frame, text="Quantidade:").pack(side="left", padx=(0, 10))
        qtd_var = ctk.IntVar(value=1)
        qtd_spin = ctk.CTkEntry(qtd_frame, textvariable=qtd_var, width=70)
        qtd_spin.pack(side="left")
        
        if tipo_item == "borda":
            qtd_spin.configure(state="disabled")
        
        # Frame dos botões
        btn_frame = ctk.CTkFrame(top, fg_color="transparent")
        btn_frame.grid(row=3, column=0, sticky="ew", padx=10, pady=10)
        
        # Configurar grid para os botões
        btn_frame.grid_columnconfigure(0, weight=1)
        btn_frame.grid_columnconfigure(1, weight=1)
        
        ctk.CTkButton(
            btn_frame,
            text="Adicionar",
            command=lambda: self.adicionar_item_handler(tree, tipo_item, qtd_var, top),
            fg_color="#4CAF50",
            hover_color="#388E3C"
        ).grid(row=0, column=0, padx=5, sticky="ew")
        
        ctk.CTkButton(
            btn_frame,
            text="Cancelar",
            command=top.destroy,
            fg_color="#F44336",
            hover_color="#D32F2F"
        ).grid(row=0, column=1, padx=5, sticky="ew")
    
    def adicionar_item_handler(self, tree, tipo_item, qtd_var, top):
        """Manipula a adição do item selecionado"""
        selecionado = tree.focus()
        if selecionado:
            item = tree.item(selecionado)['values']
            qtd = 1 if tipo_item == "borda" else qtd_var.get()
            
            self.pedido_atual['itens'].append({
                'tipo': tipo_item,
                'nome': item[1],
                'preco': float(item[2].replace("R$ ", "")),
                'quantidade': qtd
            })
            
            self.pedido_atual['total'] += float(item[2].replace("R$ ", "")) * qtd
            self.atualizar_lista_itens()
            top.destroy()
    
    def atualizar_lista_itens(self):
        """Atualiza a lista de itens no pedido"""
        self.tree_itens.delete(*self.tree_itens.get_children())
        
        for idx, item in enumerate(self.pedido_atual['itens']):
            subtotal = item['preco'] * item['quantidade']
            self.tree_itens.insert("", "end", values=(
                item['tipo'].capitalize(),
                item['nome'],
                item['quantidade'],
                f"R$ {item['preco']:.2f}",
                f"R$ {subtotal:.2f}"
            ))
        
        self.total_var.set(f"R$ {self.pedido_atual['total']:.2f}")
    
    def finalizar_pedido(self):
        """Finaliza o pedido atual e adiciona à fila"""
        if not self.pedido_atual['itens']:
            messagebox.showwarning("Aviso", "Adicione pelo menos um item ao pedido!")
            return
        
        self.pedido_atual['cliente'] = self.cliente_entry.get()
        if not self.pedido_atual['cliente']:
            messagebox.showwarning("Aviso", "Informe o nome do cliente!")
            return
        
        self.fila_pedidos.append(self.pedido_atual.copy())
        messagebox.showinfo("Sucesso", f"Pedido #{self.pedido_atual['numero']} adicionado à fila!")
        self.novo_pedido()
        self.atualizar_fila()
        self.notebook.set("Fila de Pedidos")
    
    def cancelar_pedido(self):
        """Cancela o pedido atual"""
        if messagebox.askyesno("Cancelar", "Deseja realmente cancelar este pedido?"):
            self.novo_pedido()
    
    def atualizar_fila(self):
        """Atualiza a exibição da fila de pedidos"""
        self.tree_pedidos.delete(*self.tree_pedidos.get_children())
        
        for idx, pedido in enumerate(self.fila_pedidos):
            # Agrupar itens iguais
            itens_agrupados = {}
            for item in pedido['itens']:
                chave = (item['tipo'], item['nome'], item['preco'])
                if chave in itens_agrupados:
                    itens_agrupados[chave]['quantidade'] += item['quantidade']
                else:
                    itens_agrupados[chave] = item.copy()
            
            # Formatar para exibição
            itens_formatados = []
            for item in itens_agrupados.values():
                if item['quantidade'] > 1:
                    itens_formatados.append(f"{item['quantidade']}x {item['nome']} (R${item['preco']:.2f} cada)")
                else:
                    itens_formatados.append(f"{item['nome']} (R${item['preco']:.2f})")
            
            # Inserir no treeview
            self.tree_pedidos.insert("", "end", values=(
                pedido['numero'],
                pedido['cliente'],
                f"R$ {pedido['total']:.2f}",
                "\n".join(itens_formatados)
            ))
    
    def entregar_pedido(self):
        """Marca um pedido como entregue"""
        selecionado = self.tree_pedidos.focus()
        if selecionado:
            item = self.tree_pedidos.item(selecionado)['values']
            confirmar = messagebox.askyesno(
                "Confirmar", 
                f"Entregar pedido #{item[0]} para {item[1]} no valor de {item[2]}?"
            )
            if confirmar:
                for i, pedido in enumerate(self.fila_pedidos):
                    if pedido['numero'] == int(item[0]):
                        self.fila_pedidos.pop(i)
                        break
                self.atualizar_fila()
                messagebox.showinfo("Sucesso", f"Pedido #{item[0]} entregue!")
        else:
            messagebox.showwarning("Aviso", "Selecione um pedido para entregar!")

if __name__ == "__main__":
    # Inicia com a tela de login
    login_app = LoginApp()
    login_app.login_window.mainloop()