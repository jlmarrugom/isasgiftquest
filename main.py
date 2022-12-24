import streamlit as st
import base64

st.title("Esta es la Aventura de Navidad! 🎄")

points = [0,0,0,0,0]

st.write("### Completa los retos y podrás ganar fabulosos premios! 🎁")

number = st.number_input("Reto 1: Cuantas flexiones puedes hacer? (min 8)", min_value=0, max_value=50)
but1 = st.checkbox("Validar")

if int(number) >= 8 and but1:
    st.success("Pasaste!")
    points[0] = 1
elif but1:
    st.warning("No Pasaste 😛")
    points[0] = 0

number2 = st.number_input("Reto 2: Tira un dado y saca 4 o más 🎲", min_value=0, max_value=6)
but2 = st.checkbox("Validar 2")
if int(number2) >= 4 and but2:
    st.success("Esoo!")
    points[1] = 1
elif but2:
    st.warning("Intenta de nuevo 😛")
    points[1] = 0

number3 = st.number_input("Reto 3: Abraza a cada persona de la casa en menos de 12 segundos... 3, 2, 1, Ya!", min_value=0, max_value=20, value=15)
but3 = st.checkbox("Validar 3")
if int(number3) <= 12 and but3:
    st.success("Lo superaste!")
    points[2] = 1
elif but3:
    st.warning("No te dió Juju 😛")
    points[2] = 0

number4 = st.number_input("Reto 4: Adivina el número del 0 al 25 (2 intentos)", min_value=0, max_value=25)
but4 = st.checkbox("Validar 4")

if int(number4) == 22 and but4:
    st.success("Ganaste!")
    points[3] = 1
elif but4:
    st.warning("No adivinaste 😛")
    points[3] = 0

check = st.checkbox("Reto 5: Gana en tio Rico >:)")
if check:
    st.success("-.-")
    points[4] = 1
else:
    st.warning("Juju 😛")
    points[4] = 0

premio_but = st.button("Obtener Premio Ya!")
if premio_but:
    st.balloons()
    suma_de_puntos = sum(points)
    if suma_de_puntos <= 2:
        st.image("attachments/arvalid until  22022023.png")
    elif suma_de_puntos ==3:
        st.image("attachments/k50valid until  22022023.png")
        st.image("attachments/arvalid until  22022023.png")

    elif suma_de_puntos ==4:
        st.image("attachments/k100valid until  22022023.png")
        st.image("attachments/arvalid until  22022023.png")

    elif suma_de_puntos ==5:
        st.image("attachments/k200valid until  22022023.png")
        st.image("attachments/arvalid until  22022023.png")

        