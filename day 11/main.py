import facility

# states_handled = [facility.Facility()]
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
            # next_states = state.get_next_states()
            # for next_state in next_states:
            #     handled = False
            #     for handled_state in states_handled:
            #         if handled_state.chips == next_state.chips and handled_state.generators == next_state.generators:
            #             handled = True
            #             break
            #     if not handled:
            #         states_next.append(next_state)

    if not done:
        # states_handled += states_next
        states_current = states_next
        states_next = []
        steps += 1

print('Done!', steps)
