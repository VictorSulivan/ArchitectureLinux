from routes.dtoModel.DatasourceDTO import ConditionDTO, OrderDTO


def select_filter(local_arguments, fields, order, table_fields):
    conditions = []
    for field, value in local_arguments:
        if value is not None and type(value) is not list and field in table_fields:
            conditions.append(ConditionDTO(field=field, value=str(value)))
    selected_fields = []
    if fields is not None:
        fields = fields.split(',')
        for field in fields:
            if field in table_fields:
                selected_fields.append(field)
    if not selected_fields:
        selected_fields = ["*"]
    order_by = OrderDTO(field="", type="")
    if order is not None:
        if order in table_fields:
            order_by = OrderDTO(field=order, type="asc")
        elif order[:-1] in table_fields:
            if order[-1] == "-" or order[-1] == "+":
                order_by = OrderDTO(field=order[:-1], type="asc" if order[-1] == "+" else "desc")
    else:
        order_by = OrderDTO(field="", type="")

    return [selected_fields, conditions, order_by]
