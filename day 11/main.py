import facility

states_current = [facility.Facility()]
states_next = []
steps = 0
done = False

while not done:
    print(steps, len(states_current))

    for state in states_current:
        if state.done():
            done = True
            break
        else:
            states_next += state.get_next_states()

    if not done:
        states_current = states_next
        states_next = []
        steps += 1

print('Done!', steps, 'steps')
