
print('ok')

# Add shapes
fig.update_layout(
    shapes=[
        # Quadratic Bezier Curves
        dict(
            type="path",
            path="M 4,4 Q 6,8 8,4",
            line_color="RoyalBlue",
        ),

    ]
)