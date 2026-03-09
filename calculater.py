import tkinter as tk


class NeonCalculator:
    BG       = "#0a0a0f"
    PANEL    = "#12121c"
    ENTRY_BG = "#1a1a2e"
    CYAN     = "#00f5ff"
    MAGENTA  = "#ff00cc"
    YELLOW   = "#f9ca24"
    RED      = "#ff6b6b"
    PURPLE   = "#9b59b6"
    WHITE    = "#ffffff"
    SUBTEXT  = "#666688"
    BORDER   = "#2a2a3e"

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("NEON CALC")
        self.root.geometry("460x600")
        self.root.configure(bg=self.BG)
        self.root.resizable(False, False)

        self.num1_var   = tk.StringVar()
        self.num2_var   = tk.StringVar()
        self.result_var = tk.StringVar(value="—")
        self.expr_var   = tk.StringVar(value="")

        self._build_ui()
        self._cycle_title(0)

    def _build_ui(self):
        title_frame = tk.Frame(self.root, bg=self.BG)
        title_frame.pack(pady=(22, 4))

        self.title_lbl = tk.Label(
            title_frame, text="⚡  NEON  CALC  ⚡",
            font=("Consolas", 20, "bold"), bg=self.BG, fg=self.CYAN
        )
        self.title_lbl.pack()
        tk.Label(
            title_frame, text="U L T R A  P R E C I S I O N",
            font=("Consolas", 7), bg=self.BG, fg=self.SUBTEXT
        ).pack(pady=(2, 0))

        self._hr()

        panel = tk.Frame(self.root, bg=self.PANEL)
        panel.pack(padx=28, pady=8, fill="x")

        self.e1 = self._input_row(panel, "NUMBER  1", self.num1_var, self.CYAN)
        self.e2 = self._input_row(panel, "NUMBER  2", self.num2_var, self.MAGENTA)

        self._hr()

        grid = tk.Frame(self.root, bg=self.BG)
        grid.pack(padx=28, pady=4, fill="x")
        grid.columnconfigure(0, weight=1)
        grid.columnconfigure(1, weight=1)

        specs = [
            ("+ ADD",  self.do_add, self.CYAN,    0, 0),
            ("- SUB",  self.do_sub, self.RED,     0, 1),
            ("x MUL",  self.do_mul, self.YELLOW,  1, 0),
            ("/ DIV",  self.do_div, self.MAGENTA, 1, 1),
        ]
        self._btns = []
        for text, cmd, color, row, col in specs:
            b = self._op_button(grid, text, cmd, color)
            b.grid(row=row, column=col, padx=7, pady=6, sticky="ew")
            self._btns.append((b, color))

        self._hr()

        res_panel = tk.Frame(self.root, bg=self.PANEL)
        res_panel.pack(padx=28, pady=8, fill="x")

        tk.Label(
            res_panel, text="RESULT",
            font=("Consolas", 8, "bold"), bg=self.PANEL, fg=self.SUBTEXT
        ).pack(anchor="w", padx=14, pady=(10, 0))

        self.res_lbl = tk.Label(
            res_panel, textvariable=self.result_var,
            font=("Consolas", 38, "bold"),
            bg=self.PANEL, fg=self.CYAN, anchor="e"
        )
        self.res_lbl.pack(fill="x", padx=14, pady=(2, 0))

        self.expr_lbl = tk.Label(
            res_panel, textvariable=self.expr_var,
            font=("Consolas", 10), bg=self.PANEL, fg=self.SUBTEXT, anchor="e"
        )
        self.expr_lbl.pack(fill="x", padx=14, pady=(0, 10))

        clr = tk.Button(
            self.root, text="C L E A R",
            font=("Consolas", 9, "bold"),
            bg=self.BG, fg=self.SUBTEXT, relief="flat",
            cursor="hand2", bd=0, pady=6, padx=20,
            activebackground=self.BG, activeforeground=self.WHITE,
            command=self.clear
        )
        clr.pack(pady=(2, 14))
        clr.bind("<Enter>", lambda e: clr.config(fg=self.WHITE))
        clr.bind("<Leave>", lambda e: clr.config(fg=self.SUBTEXT))

    def _hr(self):
        c = tk.Canvas(self.root, height=1, bg=self.BG, highlightthickness=0)
        c.pack(fill="x", padx=28, pady=3)
        c.create_line(0, 0, 800, 0, fill=self.BORDER, width=1)

    def _input_row(self, parent, label, var, accent):
        frame = tk.Frame(parent, bg=self.PANEL)
        frame.pack(fill="x", padx=10, pady=5)
        tk.Label(
            frame, text=label, font=("Consolas", 8, "bold"),
            bg=self.PANEL, fg=accent
        ).pack(anchor="w", padx=6, pady=(6, 0))
        e = tk.Entry(
            frame, textvariable=var,
            font=("Consolas", 17), bg=self.ENTRY_BG, fg=self.WHITE,
            insertbackground=accent, relief="flat", bd=0,
            highlightthickness=2,
            highlightcolor=accent, highlightbackground=self.BORDER
        )
        e.pack(fill="x", padx=6, pady=(2, 7), ipady=9)
        return e

    def _op_button(self, parent, text, cmd, color):
        btn = tk.Button(
            parent, text=text,
            font=("Consolas", 12, "bold"),
            bg=self.ENTRY_BG, fg=color,
            relief="flat", cursor="hand2",
            bd=0, pady=13,
            highlightthickness=1,
            highlightbackground=color,
            highlightcolor=color,
            activebackground=color,
            activeforeground="#000000",
            command=cmd
        )
        btn.bind("<Enter>", lambda e, b=btn, c=color: b.config(bg=c, fg="#000000"))
        btn.bind("<Leave>", lambda e, b=btn, c=color: b.config(bg=self.ENTRY_BG, fg=c))
        return btn

    def _nums(self):
        try:
            return float(self.num1_var.get()), float(self.num2_var.get())
        except ValueError:
            self._show("INPUT  ERR", self.RED, "Enter valid numbers in both fields")
            return None, None

    def do_add(self):
        a, b = self._nums()
        if a is not None:
            self._show(self._fmt(a + b), self.CYAN, f"{self._fmt(a)}  +  {self._fmt(b)}")
            self._flash_btn(0)

    def do_sub(self):
        a, b = self._nums()
        if a is not None:
            self._show(self._fmt(a - b), self.RED, f"{self._fmt(a)}  -  {self._fmt(b)}")
            self._flash_btn(1)

    def do_mul(self):
        a, b = self._nums()
        if a is not None:
            self._show(self._fmt(a * b), self.YELLOW, f"{self._fmt(a)}  x  {self._fmt(b)}")
            self._flash_btn(2)

    def do_div(self):
        a, b = self._nums()
        if a is not None:
            if b == 0:
                self._show("DIV / ZERO", self.MAGENTA, "Cannot divide by zero")
                return
            self._show(self._fmt(a / b), self.MAGENTA, f"{self._fmt(a)}  /  {self._fmt(b)}")
            self._flash_btn(3)

    def clear(self):
        self.num1_var.set("")
        self.num2_var.set("")
        self.result_var.set("—")
        self.expr_var.set("")
        self.res_lbl.config(fg=self.CYAN)
        self.e1.focus_set()

    def _show(self, value, color, expr=""):
        self.result_var.set(value)
        self.expr_var.set(expr)
        self._pulse_result(color, [color, self.WHITE, color, self.WHITE, color], 0)

    def _pulse_result(self, final, seq, i):
        if i < len(seq):
            self.res_lbl.config(fg=seq[i])
            self.root.after(60, self._pulse_result, final, seq, i + 1)
        else:
            self.res_lbl.config(fg=final)

    def _flash_btn(self, idx):
        btn, color = self._btns[idx]
        btn.config(bg=color, fg="#000000")
        self.root.after(160, lambda: btn.config(bg=self.ENTRY_BG, fg=color))

    def _cycle_title(self, step):
        palette = [self.CYAN, self.MAGENTA, self.PURPLE, self.YELLOW, self.MAGENTA, self.CYAN]
        self.title_lbl.config(fg=palette[step % len(palette)])
        self.root.after(700, self._cycle_title, step + 1)

    @staticmethod
    def _fmt(n):
        return str(int(n)) if n == int(n) else f"{n:.8g}"

    def run(self):
        self.e1.focus_set()
        self.root.mainloop()


if __name__ == "__main__":
    NeonCalculator().run()
