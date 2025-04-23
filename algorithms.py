from .components import FunctionalDependency, Attribute, Relvar
from itertools import combinations


def closure(attributes: set[Attribute], functional_dependencies: set[FunctionalDependency]) -> set[Attribute]:
    closure_set = set(attributes)  # Empieza con los atributos dados
    changed = True  # Controla si el cierre cambió en cada iteración

    while changed:
        changed = False
        # Recorre todas las dependencias funcionales
        for fd in functional_dependencies:
            # Si el determinante de la dependencia está en el cierre actual
            if fd.determinant <= closure_set:  # Si fd.determinant es un subconjunto de closure_set
                # Agrega los atributos dependientes al cierre
                new_elements = fd.dependant - closure_set
                if new_elements:
                    closure_set.update(new_elements)
                    changed = True  # Si el cierre cambia, establece 'changed' a True
    return closure_set


def is_superkey(attributes: set[Attribute], heading: set[Attribute], functional_dependencies: set[FunctionalDependency]) -> bool:
    return closure(attributes, functional_dependencies) == heading


def is_key(attributes: set[Attribute], heading: set[Attribute], functional_dependencies: set[FunctionalDependency]) -> bool:
    if not is_superkey(attributes, heading, functional_dependencies):
        return False
    # Verifica si hay un subconjunto propio que sea superclave  
    for i in range(1, len(attributes)):
        for subset in combinations(attributes, i):
            if is_superkey(set(subset), heading, functional_dependencies):
                return False
    return True


def is_relvar_in_bcnf(relvar: Relvar):
    for fd in relvar.functional_dependencies:
        # Si la dependencia funcional no es trivial y el determinante no es superclave
        if not fd.is_trivial() and not is_superkey(fd.determinant, relvar.heading, relvar.functional_dependencies):
            return False
    return True


def is_relvar_in_4nf(relvar: Relvar):
    if not is_relvar_in_bcnf(relvar):
        return False
    for mvd in relvar.multivalued_dependencies:
        # Si la dependencia multivaluada no es trivial y el determinante no es superclave
        if not mvd.is_trivial(relvar.heading) and not is_superkey(mvd.determinant, relvar.heading, relvar.functional_dependencies):
            return False
    return True
    
