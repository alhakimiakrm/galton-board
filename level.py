import pymunk

def create_ground(space):
    ground_body = pymunk.Body(body_type=pymunk.Body.STATIC)
    ground_body.position = (400, 500)
    ground_shape = pymunk.Segment(ground_body, (-400, 0), (400, 0), 5)
    ground_shape.elasticity = 0.8
    ground_shape.friction = 1.0
    space.add(ground_body, ground_shape)


