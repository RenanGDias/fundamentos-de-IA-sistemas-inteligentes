import numpy as np

states = ["Ensolarado", "Nublado", "Chuvoso"]

transition_matrix = [
    [0.8, 0.15, 0.05],  # Transições a partir de "Ensolarado"
    [0.2, 0.6, 0.2],    # Transições a partir de "Nublado"
    [0.25, 0.25, 0.5]   # Transições a partir de "Chuvoso"
]

initial_state = "Ensolarado"

num_days = 10

def get_state_index(state):
    return states.index(state)

def predict_weather(initial_state, num_days):
    current_state = initial_state
    forecast = [current_state]

    for _ in range(num_days - 1):
        current_index = get_state_index(current_state)
        next_state = np.random.choice(
            states, 
            p=transition_matrix[current_index]
        )
        forecast.append(next_state)
        current_state = next_state

    return forecast

forecast = predict_weather(initial_state, num_days)

print(f"Estado inicial: {initial_state}")
print("Previsão para os próximos dias:")
for day, state in enumerate(forecast, start=1):
    print(f"Dia {day}: {state}")