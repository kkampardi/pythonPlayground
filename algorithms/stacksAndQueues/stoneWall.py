solution(H):
    stack = []
    block_count = 0    # The number of needing blocks

    for height in H:
        while len(stack) != 0 and height < stack[-1]:
            # If the height of current block is less than
            #    the previous ones, the previous ones have
            #    to end before current point. They have no
            #    chance to exist in the remaining part.
            # So the previous blocks are completely finished.
            stack.pop()
            block_count += 1

        if len(stack) == 0 or height > stack[-1]:
            # If the height of current block is greater than
            #    the previous one, a new block is needed for
            #    current position.
            stack.append(height)

        # Else (the height of current block is same as that
        #    of previous one), they should be combined to
        #    one block.

    # Some blocks with different heights are still in the stack.
    block_count += len(stack)

    return block_count
