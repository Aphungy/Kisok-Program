import tkinter
import tkinter.messagebox
import customtkinter
import os
from fooditem import Sandwich, Drinks, Sides
from toppings import SandwichToppings
from PIL import Image, ImageTk 
from customtkinter import CTkImage
from File import read_sandwiches_from_file, read_drinks_from_file, read_sides_from_file, read_toppings_from_file


customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class Home(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window

        self.title("Kiosk Program")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)


        # sidebar frame 

        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Mia's Sandwhich Shop", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text= "Sandwhich",command=self.sidebar_button_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text= "Drinks",command=self.sidebar_button_event)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, text= "Sides",command=self.sidebar_button_event)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, text= "Log-out",command=self.sidebar_button_event)
        self.sidebar_button_4.grid(row=7, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))


        # Menu Frame
      
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self, label_text="Menu", width=250, height=700)
        self.scrollable_frame.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)


        # Load sandwiches from the file
      
        self.sandwiches = read_sandwiches_from_file("Fooditems.txt")


        # Create buttons for each sandwich, drink, and side
      
        row_frame = None
        button_count = 0
        for sandwich in self.sandwiches:
            sandwich_image = self.get_image(sandwich.get_image())
            if sandwich_image:
                if button_count % 3 == 0:
                    row_frame = customtkinter.CTkFrame(self.scrollable_frame)
                    row_frame.pack(fill=tkinter.X, padx=10, pady=10)
                    row_frame.grid_columnconfigure((0, 1, 2), weight=1)
                sandwich_button = customtkinter.CTkButton(row_frame, text=sandwich.get_name(), image=sandwich_image, compound="left", command=lambda s=sandwich: self.add_to_cart(s))
                sandwich_button.grid(row=0, column=button_count % 3, padx=10, pady=10)
                button_count += 1
            else:
                print(f"Error creating button for sandwich: {sandwich.get_name()}")


        # Cart Frame

        self.cart_frame = customtkinter.CTkFrame(self, width=250)
        self.cart_frame.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.cart_label = customtkinter.CTkLabel(self.cart_frame, text="Current Cart", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.cart_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.cart_textbox = customtkinter.CTkTextbox(self.cart_frame, width=200, height=650)
        self.cart_textbox.grid(row=1, column=0, padx=20, pady=(10, 0), sticky="nsew")
        #self.cart_textbox.bind("<KeyRelease>", self.update_total)
        self.lblTotal = customtkinter.CTkLabel(self.cart_frame, text="TOTAL: £0", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.lblTotal.grid(row=2, column=0, padx=5, pady=5)


        # Total variable to keep 
      
        self.total = 0.0

  
        # Functions 

  
    def get_image(self, filename):
      script_dir = os.path.dirname(os.path.abspath(__file__))
      image_path = os.path.join(script_dir, filename)

      if os.path.exists(image_path):
          return CTkImage(Image.open(image_path), size=(50, 50))
      else:
          print(f"Image '{filename}' not found.")
          return None

  
    def add_to_cart(self, sandwich):
      sandwich_item_price = float(sandwich.get_price())
      item_text = f"{sandwich.get_name()} - £{sandwich_item_price:.2f}"

      # Initialize item_price here to avoid possible unbound error
      item_price = float(sandwich_item_price)

      # Load the image
      script_dir = os.path.dirname(os.path.abspath(__file__))
      image_path = os.path.join(script_dir, sandwich.get_image())
      image = Image.open(image_path)
      photo = ImageTk.PhotoImage(image)

      # Show a confirmation dialog with the image
      confirm = tkinter.messagebox.askyesno("Add to Cart", f"Add '{sandwich.get_name()}' to cart?")

      if confirm:
          # Open a new window to select extra toppings
          toppings_window = customtkinter.CTkToplevel(self)
          toppings_window.title("Select Extra Toppings")
          toppings_window.geometry("300x400")
  
          self.extra_toppings = read_toppings_from_file("Toppings.txt")
  
          # Create a frame for the checkboxes
          toppings_frame = customtkinter.CTkFrame(toppings_window)
          toppings_frame.pack(padx=20, pady=20, fill=tkinter.BOTH, expand=True)
  
          # Create a list to store the checkbox variables
          self.toppings_vars = []
        
          # Create checkboxes for each topping
          for topping in self.extra_toppings:
              var = tkinter.IntVar()
              checkbox = customtkinter.CTkCheckBox(toppings_frame, text=f"{topping.get_name()} - £{topping.get_price()}", variable=var)
              checkbox.pack(anchor="w", padx=10, pady=5)
              self.toppings_vars.append(var)

          def add_toppings_and_item(self):
              selected_toppings = []
              item_price = 0.0  
              for var, topping in zip(self.toppings_vars, self.extra_toppings):
                  if var.get() == 1:
                      selected_toppings.append(topping.get_name())
                      item_price += float(topping.get_price())

              if selected_toppings:
                  toppings_text = ", ".join(selected_toppings)
                  item_text_with_toppings = f"{item_text} (with {toppings_text} - £{item_price: .2f})"
              else:
                  item_text_with_toppings = item_text

              self.cart_textbox.insert("0.0", item_text_with_toppings + "\n")
              self.total += sandwich_item_price + item_price
              self.lblTotal.configure(text=f"TOTAL: £{self.total:.2f}")

              toppings_window.destroy()

          add_button = customtkinter.CTkButton(toppings_window, text="Add to Cart", command=lambda: add_toppings_and_item(self))
          add_button.pack(pady=10)
      else:
          # User clicked "No" on the confirmation dialog
          pass

  
    def update_total(self, event=None):
      self.total = 0.0
      cart_items = self.cart_textbox.get("0.0", "end-1c").splitlines()
      for item in cart_items:
          item_parts = item.split(" - £")
          if len(item_parts) == 2:
              try:
                  item_price = float(item_parts[1])
                  self.total += item_price
              except ValueError:
                  pass
      self.lblTotal.configure(text=f"TOTAL: £{self.total:.2f}")

  
    def change_appearance_mode_event(self, new_appearance_mode: str):
      customtkinter.set_appearance_mode(new_appearance_mode)

  
    def sidebar_button_event(self):       
        #dialog = customtkinter.CTkButton(text="Type in a number:", title="CTkButton")
        #print("CTkButton:", dialog.get_input())
        pass


if __name__ == "__main__":
      home = Home()
      home.mainloop()
