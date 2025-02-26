class Checks:
    resolved_move = True

    def position(self, int_obj, ext_obj):
        if int_obj.rect.left <= ext_obj.left:
            int_obj.rect.left = ext_obj.left
            self.resolved_move = False

        if int_obj.rect.right >= ext_obj.right:
            int_obj.rect.right = ext_obj.right
            self.resolved_move = False

        if int_obj.rect.top <= ext_obj.top:
            int_obj.rect.top = ext_obj.top
            self.resolved_move = False

        if int_obj.rect.bottom >= ext_obj.bottom:
            int_obj.rect.bottom = ext_obj.bottom
            self.resolved_move = False