# Auto generated from rhea.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-01-10T13:21:49
# Schema: rhea-linkml
#
# id: https://w3id.org/rhea
# description: Experimental alpha version of a rendering of Rhea as LinkML For additional context, see
#              [linkml-rhea docs](https://chemkg.github.io/linkml-rhea/home) This schema should largely correspond
#              one-to-one with classes and properties in Rhea. Modifications: * Added a AbstractReaction grouping
#              * prefixed properties directional/bidirectionalReaction with 'has' * mkdocs requires
#              case-insensitive names, so this avoids name clash with classes * we retain the true rdf property as
#              slot_uri
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Boolean, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
CHEMROF = CurieNamespace('chemrof', 'https://w3id.org/chemrof/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
RHEA = CurieNamespace('rhea', 'http://rdf.rhea-db.org/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = RHEA


# Types
class DatabaseIdentifier(Uriorcurie):
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "Database identifier"
    type_model_uri = RHEA.DatabaseIdentifier


class CHEBIIdentifier(DatabaseIdentifier):
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "CHEBI identifier"
    type_model_uri = RHEA.CHEBIIdentifier


# Class references
class ClassId(URIorCURIE):
    pass


class AbstractReactionId(ClassId):
    pass


class ReactionId(AbstractReactionId):
    pass


class DirectionalReactionId(AbstractReactionId):
    pass


class BidirectionalReactionId(AbstractReactionId):
    pass


class ReactionParticipantId(ClassId):
    pass


class ReactionSideId(URIorCURIE):
    pass


class ReactivePartId(ClassId):
    pass


class CompoundId(ClassId):
    pass


class SmallMoleculeId(CompoundId):
    pass


class GenericCompoundId(CompoundId):
    pass


class GenericPolynucleotideId(GenericCompoundId):
    pass


class GenericPolypeptideId(GenericCompoundId):
    pass


class PolymerId(CompoundId):
    pass


@dataclass
class Class(YAMLRoot):
    """
    compounds and reactions are represented as classes in Rhea
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RDFS.Class
    class_class_curie: ClassVar[str] = "rdfs:Class"
    class_name: ClassVar[str] = "Class"
    class_model_uri: ClassVar[URIRef] = RHEA.Class

    id: Union[Union[str, ClassId], List[Union[str, ClassId]]] = None
    comment: Optional[str] = None
    type: Optional[Union[str, URIorCURIE]] = None
    label: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, list):
            self.id = [self.id] if self.id is not None else []
        self.id = [v if isinstance(v, ClassId) else ClassId(v) for v in self.id]

        if self.comment is not None and not isinstance(self.comment, str):
            self.comment = str(self.comment)

        if self.type is not None and not isinstance(self.type, URIorCURIE):
            self.type = URIorCURIE(self.type)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        super().__post_init__(**kwargs)


@dataclass
class AbstractReaction(Class):
    """
    Grouping class for all three reaction forms
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RHEA.AbstractReaction
    class_class_curie: ClassVar[str] = "rhea:AbstractReaction"
    class_name: ClassVar[str] = "AbstractReaction"
    class_model_uri: ClassVar[URIRef] = RHEA.AbstractReaction

    id: Union[Union[str, AbstractReactionId], List[Union[str, AbstractReactionId]]] = None
    status: Optional[Union[str, "StatusEnum"]] = None
    accession: Optional[Union[str, DatabaseIdentifier]] = None
    seeAlso: Optional[Union[str, List[str]]] = empty_list()
    isTransport: Optional[Union[bool, Bool]] = None
    isChemicallyBalanced: Optional[Union[bool, Bool]] = None
    citation: Optional[Union[int, List[int]]] = empty_list()
    htmlEquation: Optional[str] = None
    equation: Optional[str] = None
    subClassOf: Optional[Union[str, AbstractReactionId]] = None
    ec: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.status is not None and not isinstance(self.status, StatusEnum):
            self.status = StatusEnum(self.status)

        if self.accession is not None and not isinstance(self.accession, DatabaseIdentifier):
            self.accession = DatabaseIdentifier(self.accession)

        if not isinstance(self.seeAlso, list):
            self.seeAlso = [self.seeAlso] if self.seeAlso is not None else []
        self.seeAlso = [v if isinstance(v, str) else str(v) for v in self.seeAlso]

        if self.isTransport is not None and not isinstance(self.isTransport, Bool):
            self.isTransport = Bool(self.isTransport)

        if self.isChemicallyBalanced is not None and not isinstance(self.isChemicallyBalanced, Bool):
            self.isChemicallyBalanced = Bool(self.isChemicallyBalanced)

        if not isinstance(self.citation, list):
            self.citation = [self.citation] if self.citation is not None else []
        self.citation = [v if isinstance(v, int) else int(v) for v in self.citation]

        if self.htmlEquation is not None and not isinstance(self.htmlEquation, str):
            self.htmlEquation = str(self.htmlEquation)

        if self.equation is not None and not isinstance(self.equation, str):
            self.equation = str(self.equation)

        if self.subClassOf is not None and not isinstance(self.subClassOf, AbstractReactionId):
            self.subClassOf = AbstractReactionId(self.subClassOf)

        if not isinstance(self.ec, list):
            self.ec = [self.ec] if self.ec is not None else []
        self.ec = [v if isinstance(v, str) else str(v) for v in self.ec]

        super().__post_init__(**kwargs)


@dataclass
class Reaction(AbstractReaction):
    """
    A chemical reaction, with unspecified direction.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RHEA.Reaction
    class_class_curie: ClassVar[str] = "rhea:Reaction"
    class_name: ClassVar[str] = "Reaction"
    class_model_uri: ClassVar[URIRef] = RHEA.Reaction

    id: Union[Union[str, ReactionId], List[Union[str, ReactionId]]] = None
    hasDirectionalReaction: Optional[Union[Union[str, DirectionalReactionId], List[Union[str, DirectionalReactionId]]]] = empty_list()
    hasBidirectionalReaction: Optional[Union[str, BidirectionalReactionId]] = None
    side: Optional[Union[Union[str, ReactionSideId], List[Union[str, ReactionSideId]]]] = empty_list()
    ec: Optional[Union[str, List[str]]] = empty_list()
    subClassOf: Optional[Union[str, ReactionId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, list):
            self.id = [self.id] if self.id is not None else []
        self.id = [v if isinstance(v, ReactionId) else ReactionId(v) for v in self.id]

        if not isinstance(self.hasDirectionalReaction, list):
            self.hasDirectionalReaction = [self.hasDirectionalReaction] if self.hasDirectionalReaction is not None else []
        self.hasDirectionalReaction = [v if isinstance(v, DirectionalReactionId) else DirectionalReactionId(v) for v in self.hasDirectionalReaction]

        if self.hasBidirectionalReaction is not None and not isinstance(self.hasBidirectionalReaction, BidirectionalReactionId):
            self.hasBidirectionalReaction = BidirectionalReactionId(self.hasBidirectionalReaction)

        if not isinstance(self.side, list):
            self.side = [self.side] if self.side is not None else []
        self.side = [v if isinstance(v, ReactionSideId) else ReactionSideId(v) for v in self.side]

        if not isinstance(self.ec, list):
            self.ec = [self.ec] if self.ec is not None else []
        self.ec = [v if isinstance(v, str) else str(v) for v in self.ec]

        if self.subClassOf is not None and not isinstance(self.subClassOf, ReactionId):
            self.subClassOf = ReactionId(self.subClassOf)

        super().__post_init__(**kwargs)


@dataclass
class DirectionalReaction(AbstractReaction):
    """
    A chemical reaction, with the direction specified by substrates and products.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RHEA.DirectionalReaction
    class_class_curie: ClassVar[str] = "rhea:DirectionalReaction"
    class_name: ClassVar[str] = "DirectionalReaction"
    class_model_uri: ClassVar[URIRef] = RHEA.DirectionalReaction

    id: Union[Union[str, DirectionalReactionId], List[Union[str, DirectionalReactionId]]] = None
    substrates: Optional[Union[str, ReactionSideId]] = None
    products: Optional[Union[str, ReactionSideId]] = None
    subClassOf: Optional[Union[str, DirectionalReactionId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, list):
            self.id = [self.id] if self.id is not None else []
        self.id = [v if isinstance(v, DirectionalReactionId) else DirectionalReactionId(v) for v in self.id]

        if self.substrates is not None and not isinstance(self.substrates, ReactionSideId):
            self.substrates = ReactionSideId(self.substrates)

        if self.products is not None and not isinstance(self.products, ReactionSideId):
            self.products = ReactionSideId(self.products)

        if self.subClassOf is not None and not isinstance(self.subClassOf, DirectionalReactionId):
            self.subClassOf = DirectionalReactionId(self.subClassOf)

        super().__post_init__(**kwargs)


@dataclass
class BidirectionalReaction(AbstractReaction):
    """
    A chemical reaction which can happen in one direction or the other, depending on the physiological conditions.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RHEA.BidirectionalReaction
    class_class_curie: ClassVar[str] = "rhea:BidirectionalReaction"
    class_name: ClassVar[str] = "BidirectionalReaction"
    class_model_uri: ClassVar[URIRef] = RHEA.BidirectionalReaction

    id: Union[Union[str, BidirectionalReactionId], List[Union[str, BidirectionalReactionId]]] = None
    substratesOrProducts: Optional[Union[Union[str, ReactionSideId], List[Union[str, ReactionSideId]]]] = empty_list()
    subClassOf: Optional[Union[str, BidirectionalReactionId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, list):
            self.id = [self.id] if self.id is not None else []
        self.id = [v if isinstance(v, BidirectionalReactionId) else BidirectionalReactionId(v) for v in self.id]

        if not isinstance(self.substratesOrProducts, list):
            self.substratesOrProducts = [self.substratesOrProducts] if self.substratesOrProducts is not None else []
        self.substratesOrProducts = [v if isinstance(v, ReactionSideId) else ReactionSideId(v) for v in self.substratesOrProducts]

        if self.subClassOf is not None and not isinstance(self.subClassOf, BidirectionalReactionId):
            self.subClassOf = BidirectionalReactionId(self.subClassOf)

        super().__post_init__(**kwargs)


@dataclass
class ReactionParticipant(Class):
    """
    A reaction participant. Contained in a reaction side.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RHEA.ReactionParticipant
    class_class_curie: ClassVar[str] = "rhea:ReactionParticipant"
    class_name: ClassVar[str] = "ReactionParticipant"
    class_model_uri: ClassVar[URIRef] = RHEA.ReactionParticipant

    id: Union[Union[str, ReactionParticipantId], List[Union[str, ReactionParticipantId]]] = None
    compound: Optional[Union[str, CompoundId]] = None
    location: Optional[Union[str, "LocationEnum"]] = None
    subClassOf: Optional[Union[str, CompoundId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, list):
            self.id = [self.id] if self.id is not None else []
        self.id = [v if isinstance(v, ReactionParticipantId) else ReactionParticipantId(v) for v in self.id]

        if self.compound is not None and not isinstance(self.compound, CompoundId):
            self.compound = CompoundId(self.compound)

        if self.location is not None and not isinstance(self.location, LocationEnum):
            self.location = LocationEnum(self.location)

        if self.subClassOf is not None and not isinstance(self.subClassOf, CompoundId):
            self.subClassOf = CompoundId(self.subClassOf)

        super().__post_init__(**kwargs)


@dataclass
class ReactionSide(YAMLRoot):
    """
    A reaction side in a chemical reaction. Contains one or more reaction participants.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RHEA.ReactionSide
    class_class_curie: ClassVar[str] = "rhea:ReactionSide"
    class_name: ClassVar[str] = "ReactionSide"
    class_model_uri: ClassVar[URIRef] = RHEA.ReactionSide

    id: Union[Union[str, ReactionSideId], List[Union[str, ReactionSideId]]] = None
    contains: Optional[Union[Union[str, ReactionParticipantId], List[Union[str, ReactionParticipantId]]]] = empty_list()
    transformableTo: Optional[Union[str, ReactionSideId]] = None
    type: Optional[Union[str, URIorCURIE]] = None
    curatedOrder: Optional[int] = None
    contains1: Optional[Union[str, List[str]]] = empty_list()
    contains2: Optional[Union[str, List[str]]] = empty_list()
    contains4: Optional[Union[str, List[str]]] = empty_list()
    contains3: Optional[Union[str, List[str]]] = empty_list()
    contains6: Optional[Union[str, List[str]]] = empty_list()
    contains5: Optional[Union[str, List[str]]] = empty_list()
    contains8: Optional[Union[str, List[str]]] = empty_list()
    containsN: Optional[Union[str, List[str]]] = empty_list()
    contains7: Optional[Union[str, List[str]]] = empty_list()
    contains16: Optional[Union[str, List[str]]] = empty_list()
    contains9: Optional[Union[str, List[str]]] = empty_list()
    contains20: Optional[Union[str, List[str]]] = empty_list()
    contains11: Optional[Union[str, List[str]]] = empty_list()
    contains12: Optional[Union[str, List[str]]] = empty_list()
    containsNminus1: Optional[Union[str, List[str]]] = empty_list()
    contains2n: Optional[Union[str, List[str]]] = empty_list()
    contains10: Optional[Union[str, List[str]]] = empty_list()
    contains22: Optional[Union[str, List[str]]] = empty_list()
    contains24: Optional[Union[str, List[str]]] = empty_list()
    containsNplus1: Optional[Union[str, List[str]]] = empty_list()
    contains27: Optional[Union[str, List[str]]] = empty_list()
    contains18: Optional[Union[str, List[str]]] = empty_list()
    contains28: Optional[Union[str, List[str]]] = empty_list()
    contains32: Optional[Union[str, List[str]]] = empty_list()
    contains17: Optional[Union[str, List[str]]] = empty_list()
    contains13: Optional[Union[str, List[str]]] = empty_list()
    contains14: Optional[Union[str, List[str]]] = empty_list()
    contains40: Optional[Union[str, List[str]]] = empty_list()
    contains26: Optional[Union[str, List[str]]] = empty_list()
    contains21: Optional[Union[str, List[str]]] = empty_list()
    contains19: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, list):
            self.id = [self.id] if self.id is not None else []
        self.id = [v if isinstance(v, ReactionSideId) else ReactionSideId(v) for v in self.id]

        if not isinstance(self.contains, list):
            self.contains = [self.contains] if self.contains is not None else []
        self.contains = [v if isinstance(v, ReactionParticipantId) else ReactionParticipantId(v) for v in self.contains]

        if self.transformableTo is not None and not isinstance(self.transformableTo, ReactionSideId):
            self.transformableTo = ReactionSideId(self.transformableTo)

        if self.type is not None and not isinstance(self.type, URIorCURIE):
            self.type = URIorCURIE(self.type)

        if self.curatedOrder is not None and not isinstance(self.curatedOrder, int):
            self.curatedOrder = int(self.curatedOrder)

        if not isinstance(self.contains1, list):
            self.contains1 = [self.contains1] if self.contains1 is not None else []
        self.contains1 = [v if isinstance(v, str) else str(v) for v in self.contains1]

        if not isinstance(self.contains2, list):
            self.contains2 = [self.contains2] if self.contains2 is not None else []
        self.contains2 = [v if isinstance(v, str) else str(v) for v in self.contains2]

        if not isinstance(self.contains4, list):
            self.contains4 = [self.contains4] if self.contains4 is not None else []
        self.contains4 = [v if isinstance(v, str) else str(v) for v in self.contains4]

        if not isinstance(self.contains3, list):
            self.contains3 = [self.contains3] if self.contains3 is not None else []
        self.contains3 = [v if isinstance(v, str) else str(v) for v in self.contains3]

        if not isinstance(self.contains6, list):
            self.contains6 = [self.contains6] if self.contains6 is not None else []
        self.contains6 = [v if isinstance(v, str) else str(v) for v in self.contains6]

        if not isinstance(self.contains5, list):
            self.contains5 = [self.contains5] if self.contains5 is not None else []
        self.contains5 = [v if isinstance(v, str) else str(v) for v in self.contains5]

        if not isinstance(self.contains8, list):
            self.contains8 = [self.contains8] if self.contains8 is not None else []
        self.contains8 = [v if isinstance(v, str) else str(v) for v in self.contains8]

        if not isinstance(self.containsN, list):
            self.containsN = [self.containsN] if self.containsN is not None else []
        self.containsN = [v if isinstance(v, str) else str(v) for v in self.containsN]

        if not isinstance(self.contains7, list):
            self.contains7 = [self.contains7] if self.contains7 is not None else []
        self.contains7 = [v if isinstance(v, str) else str(v) for v in self.contains7]

        if not isinstance(self.contains16, list):
            self.contains16 = [self.contains16] if self.contains16 is not None else []
        self.contains16 = [v if isinstance(v, str) else str(v) for v in self.contains16]

        if not isinstance(self.contains9, list):
            self.contains9 = [self.contains9] if self.contains9 is not None else []
        self.contains9 = [v if isinstance(v, str) else str(v) for v in self.contains9]

        if not isinstance(self.contains20, list):
            self.contains20 = [self.contains20] if self.contains20 is not None else []
        self.contains20 = [v if isinstance(v, str) else str(v) for v in self.contains20]

        if not isinstance(self.contains11, list):
            self.contains11 = [self.contains11] if self.contains11 is not None else []
        self.contains11 = [v if isinstance(v, str) else str(v) for v in self.contains11]

        if not isinstance(self.contains12, list):
            self.contains12 = [self.contains12] if self.contains12 is not None else []
        self.contains12 = [v if isinstance(v, str) else str(v) for v in self.contains12]

        if not isinstance(self.containsNminus1, list):
            self.containsNminus1 = [self.containsNminus1] if self.containsNminus1 is not None else []
        self.containsNminus1 = [v if isinstance(v, str) else str(v) for v in self.containsNminus1]

        if not isinstance(self.contains2n, list):
            self.contains2n = [self.contains2n] if self.contains2n is not None else []
        self.contains2n = [v if isinstance(v, str) else str(v) for v in self.contains2n]

        if not isinstance(self.contains10, list):
            self.contains10 = [self.contains10] if self.contains10 is not None else []
        self.contains10 = [v if isinstance(v, str) else str(v) for v in self.contains10]

        if not isinstance(self.contains22, list):
            self.contains22 = [self.contains22] if self.contains22 is not None else []
        self.contains22 = [v if isinstance(v, str) else str(v) for v in self.contains22]

        if not isinstance(self.contains24, list):
            self.contains24 = [self.contains24] if self.contains24 is not None else []
        self.contains24 = [v if isinstance(v, str) else str(v) for v in self.contains24]

        if not isinstance(self.containsNplus1, list):
            self.containsNplus1 = [self.containsNplus1] if self.containsNplus1 is not None else []
        self.containsNplus1 = [v if isinstance(v, str) else str(v) for v in self.containsNplus1]

        if not isinstance(self.contains27, list):
            self.contains27 = [self.contains27] if self.contains27 is not None else []
        self.contains27 = [v if isinstance(v, str) else str(v) for v in self.contains27]

        if not isinstance(self.contains18, list):
            self.contains18 = [self.contains18] if self.contains18 is not None else []
        self.contains18 = [v if isinstance(v, str) else str(v) for v in self.contains18]

        if not isinstance(self.contains28, list):
            self.contains28 = [self.contains28] if self.contains28 is not None else []
        self.contains28 = [v if isinstance(v, str) else str(v) for v in self.contains28]

        if not isinstance(self.contains32, list):
            self.contains32 = [self.contains32] if self.contains32 is not None else []
        self.contains32 = [v if isinstance(v, str) else str(v) for v in self.contains32]

        if not isinstance(self.contains17, list):
            self.contains17 = [self.contains17] if self.contains17 is not None else []
        self.contains17 = [v if isinstance(v, str) else str(v) for v in self.contains17]

        if not isinstance(self.contains13, list):
            self.contains13 = [self.contains13] if self.contains13 is not None else []
        self.contains13 = [v if isinstance(v, str) else str(v) for v in self.contains13]

        if not isinstance(self.contains14, list):
            self.contains14 = [self.contains14] if self.contains14 is not None else []
        self.contains14 = [v if isinstance(v, str) else str(v) for v in self.contains14]

        if not isinstance(self.contains40, list):
            self.contains40 = [self.contains40] if self.contains40 is not None else []
        self.contains40 = [v if isinstance(v, str) else str(v) for v in self.contains40]

        if not isinstance(self.contains26, list):
            self.contains26 = [self.contains26] if self.contains26 is not None else []
        self.contains26 = [v if isinstance(v, str) else str(v) for v in self.contains26]

        if not isinstance(self.contains21, list):
            self.contains21 = [self.contains21] if self.contains21 is not None else []
        self.contains21 = [v if isinstance(v, str) else str(v) for v in self.contains21]

        if not isinstance(self.contains19, list):
            self.contains19 = [self.contains19] if self.contains19 is not None else []
        self.contains19 = [v if isinstance(v, str) else str(v) for v in self.contains19]

        super().__post_init__(**kwargs)


@dataclass
class ReactivePart(Class):
    """
    A reactive part in a generic compound, with a defined chemical structure. A subclass of a given ChEBI chemical
    entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RHEA.ReactivePart
    class_class_curie: ClassVar[str] = "rhea:ReactivePart"
    class_name: ClassVar[str] = "ReactivePart"
    class_model_uri: ClassVar[URIRef] = RHEA.ReactivePart

    id: Union[Union[str, ReactivePartId], List[Union[str, ReactivePartId]]] = None
    name: Optional[str] = None
    charge: Optional[int] = None
    chebi: Optional[str] = None
    formula: Optional[str] = None
    htmlName: Optional[str] = None
    position: Optional[int] = None
    subClassOf: Optional[Union[str, CompoundId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, list):
            self.id = [self.id] if self.id is not None else []
        self.id = [v if isinstance(v, ReactivePartId) else ReactivePartId(v) for v in self.id]

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.charge is not None and not isinstance(self.charge, int):
            self.charge = int(self.charge)

        if self.chebi is not None and not isinstance(self.chebi, str):
            self.chebi = str(self.chebi)

        if self.formula is not None and not isinstance(self.formula, str):
            self.formula = str(self.formula)

        if self.htmlName is not None and not isinstance(self.htmlName, str):
            self.htmlName = str(self.htmlName)

        if self.position is not None and not isinstance(self.position, int):
            self.position = int(self.position)

        if self.subClassOf is not None and not isinstance(self.subClassOf, CompoundId):
            self.subClassOf = CompoundId(self.subClassOf)

        super().__post_init__(**kwargs)


@dataclass
class Compound(Class):
    """
    A chemical compound
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RHEA.Compound
    class_class_curie: ClassVar[str] = "rhea:Compound"
    class_name: ClassVar[str] = "Compound"
    class_model_uri: ClassVar[URIRef] = RHEA.Compound

    id: Union[Union[str, CompoundId], List[Union[str, CompoundId]]] = None
    name: Optional[str] = None
    accession: Optional[Union[str, DatabaseIdentifier]] = None
    htmlName: Optional[str] = None
    formula: Optional[str] = None
    subClassOf: Optional[Union[str, CompoundId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, list):
            self.id = [self.id] if self.id is not None else []
        self.id = [v if isinstance(v, CompoundId) else CompoundId(v) for v in self.id]

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.accession is not None and not isinstance(self.accession, DatabaseIdentifier):
            self.accession = DatabaseIdentifier(self.accession)

        if self.htmlName is not None and not isinstance(self.htmlName, str):
            self.htmlName = str(self.htmlName)

        if self.formula is not None and not isinstance(self.formula, str):
            self.formula = str(self.formula)

        if self.subClassOf is not None and not isinstance(self.subClassOf, CompoundId):
            self.subClassOf = CompoundId(self.subClassOf)

        super().__post_init__(**kwargs)


@dataclass
class SmallMolecule(Compound):
    """
    A chemical compound that is a small molecule. A subclass of a given ChEBI chemical entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RHEA.SmallMolecule
    class_class_curie: ClassVar[str] = "rhea:SmallMolecule"
    class_name: ClassVar[str] = "SmallMolecule"
    class_model_uri: ClassVar[URIRef] = RHEA.SmallMolecule

    id: Union[Union[str, SmallMoleculeId], List[Union[str, SmallMoleculeId]]] = None
    chebi: Optional[str] = None
    htmlName: Optional[str] = None
    charge: Optional[int] = None
    name: Optional[str] = None
    subClassOf: Optional[Union[str, SmallMoleculeId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, list):
            self.id = [self.id] if self.id is not None else []
        self.id = [v if isinstance(v, SmallMoleculeId) else SmallMoleculeId(v) for v in self.id]

        if self.chebi is not None and not isinstance(self.chebi, str):
            self.chebi = str(self.chebi)

        if self.htmlName is not None and not isinstance(self.htmlName, str):
            self.htmlName = str(self.htmlName)

        if self.charge is not None and not isinstance(self.charge, int):
            self.charge = int(self.charge)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.subClassOf is not None and not isinstance(self.subClassOf, SmallMoleculeId):
            self.subClassOf = SmallMoleculeId(self.subClassOf)

        super().__post_init__(**kwargs)


@dataclass
class GenericCompound(Compound):
    """
    A chemical compound whose complete chemical structure is not described. Have one or or more reactive part(s) with
    chemical structure(s).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RHEA.GenericCompound
    class_class_curie: ClassVar[str] = "rhea:GenericCompound"
    class_name: ClassVar[str] = "GenericCompound"
    class_model_uri: ClassVar[URIRef] = RHEA.GenericCompound

    id: Union[Union[str, GenericCompoundId], List[Union[str, GenericCompoundId]]] = None
    reactivePart: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, list):
            self.id = [self.id] if self.id is not None else []
        self.id = [v if isinstance(v, GenericCompoundId) else GenericCompoundId(v) for v in self.id]

        if not isinstance(self.reactivePart, list):
            self.reactivePart = [self.reactivePart] if self.reactivePart is not None else []
        self.reactivePart = [v if isinstance(v, str) else str(v) for v in self.reactivePart]

        super().__post_init__(**kwargs)


@dataclass
class GenericPolynucleotide(GenericCompound):
    """
    A generic compound that is a polynucleotide. Have one or or more reactive part(s) with chemical structure(s).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RHEA.GenericPolynucleotide
    class_class_curie: ClassVar[str] = "rhea:GenericPolynucleotide"
    class_name: ClassVar[str] = "GenericPolynucleotide"
    class_model_uri: ClassVar[URIRef] = RHEA.GenericPolynucleotide

    id: Union[Union[str, GenericPolynucleotideId], List[Union[str, GenericPolynucleotideId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, list):
            self.id = [self.id] if self.id is not None else []
        self.id = [v if isinstance(v, GenericPolynucleotideId) else GenericPolynucleotideId(v) for v in self.id]

        super().__post_init__(**kwargs)


@dataclass
class GenericPolypeptide(GenericCompound):
    """
    A generic compound that is a polypeptide. Have one or or more reactive part(s) with chemical structure(s).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RHEA.GenericPolypeptide
    class_class_curie: ClassVar[str] = "rhea:GenericPolypeptide"
    class_name: ClassVar[str] = "GenericPolypeptide"
    class_model_uri: ClassVar[URIRef] = RHEA.GenericPolypeptide

    id: Union[Union[str, GenericPolypeptideId], List[Union[str, GenericPolypeptideId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, list):
            self.id = [self.id] if self.id is not None else []
        self.id = [v if isinstance(v, GenericPolypeptideId) else GenericPolypeptideId(v) for v in self.id]

        super().__post_init__(**kwargs)


@dataclass
class Polymer(Compound):
    """
    A chemical compound that is a polymer. Described by a polymerization index, and an underlying polymer from ChEBI.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RHEA.Polymer
    class_class_curie: ClassVar[str] = "rhea:Polymer"
    class_name: ClassVar[str] = "Polymer"
    class_model_uri: ClassVar[URIRef] = RHEA.Polymer

    id: Union[Union[str, PolymerId], List[Union[str, PolymerId]]] = None
    charge: Optional[int] = None
    underlyingChebi: Optional[Union[str, CHEBIIdentifier]] = None
    polymerizationIndex: Optional[Union[str, "PolymerizationIndexEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, list):
            self.id = [self.id] if self.id is not None else []
        self.id = [v if isinstance(v, PolymerId) else PolymerId(v) for v in self.id]

        if self.charge is not None and not isinstance(self.charge, int):
            self.charge = int(self.charge)

        if self.underlyingChebi is not None and not isinstance(self.underlyingChebi, CHEBIIdentifier):
            self.underlyingChebi = CHEBIIdentifier(self.underlyingChebi)

        if self.polymerizationIndex is not None and not isinstance(self.polymerizationIndex, PolymerizationIndexEnum):
            self.polymerizationIndex = PolymerizationIndexEnum(self.polymerizationIndex)

        super().__post_init__(**kwargs)


# Enumerations
class LocationEnum(EnumDefinitionImpl):

    Out = PermissibleValue(text="Out",
                             description="Out",
                             meaning=RHEA.Out)
    In = PermissibleValue(text="In",
                           description="In",
                           meaning=RHEA.In)

    _defn = EnumDefinition(
        name="LocationEnum",
    )

class StatusEnum(EnumDefinitionImpl):

    Approved = PermissibleValue(text="Approved",
                                       description="Approved",
                                       meaning=RHEA.Approved)
    Obsolete = PermissibleValue(text="Obsolete",
                                       description="Obsolete",
                                       meaning=RHEA.Obsolete)
    Preliminary = PermissibleValue(text="Preliminary",
                                             description="Preliminary",
                                             meaning=RHEA.Preliminary)

    _defn = EnumDefinition(
        name="StatusEnum",
    )

class PolymerizationIndexEnum(EnumDefinitionImpl):

    n = PermissibleValue(text="n",
                         description="n")

    _defn = EnumDefinition(
        name="PolymerizationIndexEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "n-2",
                PermissibleValue(text="n-2",
                                 description="n-2") )
        setattr(cls, "n+1",
                PermissibleValue(text="n+1",
                                 description="n+1") )
        setattr(cls, "n-3",
                PermissibleValue(text="n-3",
                                 description="n-3") )
        setattr(cls, "n-1",
                PermissibleValue(text="n-1",
                                 description="n-1") )
        setattr(cls, "n-5",
                PermissibleValue(text="n-5",
                                 description="n-5") )
        setattr(cls, "n-4",
                PermissibleValue(text="n-4",
                                 description="n-4") )
        setattr(cls, "n+2",
                PermissibleValue(text="n+2",
                                 description="n+2") )

# Slots
class slots:
    pass

slots.id = Slot(uri=RHEA.id, name="id", curie=RHEA.curie('id'),
                   model_uri=RHEA.id, domain=None, range=URIRef)

slots.name = Slot(uri=RHEA.name, name="name", curie=RHEA.curie('name'),
                   model_uri=RHEA.name, domain=None, range=Optional[str])

slots.accession = Slot(uri=RHEA.accession, name="accession", curie=RHEA.curie('accession'),
                   model_uri=RHEA.accession, domain=None, range=Optional[Union[str, DatabaseIdentifier]])

slots.chebi = Slot(uri=RHEA.chebi, name="chebi", curie=RHEA.curie('chebi'),
                   model_uri=RHEA.chebi, domain=None, range=Optional[str])

slots.htmlName = Slot(uri=RHEA.htmlName, name="htmlName", curie=RHEA.curie('htmlName'),
                   model_uri=RHEA.htmlName, domain=None, range=Optional[str])

slots.status = Slot(uri=RHEA.status, name="status", curie=RHEA.curie('status'),
                   model_uri=RHEA.status, domain=None, range=Optional[Union[str, "StatusEnum"]])

slots.label = Slot(uri=RDFS.label, name="label", curie=RDFS.curie('label'),
                   model_uri=RHEA.label, domain=None, range=Optional[str])

slots.seeAlso = Slot(uri=RDFS.seeAlso, name="seeAlso", curie=RDFS.curie('seeAlso'),
                   model_uri=RHEA.seeAlso, domain=None, range=Optional[Union[str, List[str]]])

slots.comment = Slot(uri=RDFS.comment, name="comment", curie=RDFS.curie('comment'),
                   model_uri=RHEA.comment, domain=None, range=Optional[str])

slots.citation = Slot(uri=RHEA.citation, name="citation", curie=RHEA.curie('citation'),
                   model_uri=RHEA.citation, domain=None, range=Optional[Union[int, List[int]]])

slots.type = Slot(uri=RDF.type, name="type", curie=RDF.curie('type'),
                   model_uri=RHEA.type, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.subClassOf = Slot(uri=RDFS.subClassOf, name="subClassOf", curie=RDFS.curie('subClassOf'),
                   model_uri=RHEA.subClassOf, domain=None, range=Optional[Union[str, ClassId]])

slots.formula = Slot(uri=RHEA.formula, name="formula", curie=RHEA.curie('formula'),
                   model_uri=RHEA.formula, domain=None, range=Optional[str])

slots.charge = Slot(uri=RHEA.charge, name="charge", curie=RHEA.curie('charge'),
                   model_uri=RHEA.charge, domain=None, range=Optional[int])

slots.equation = Slot(uri=RHEA.equation, name="equation", curie=RHEA.curie('equation'),
                   model_uri=RHEA.equation, domain=None, range=Optional[str])

slots.htmlEquation = Slot(uri=RHEA.htmlEquation, name="htmlEquation", curie=RHEA.curie('htmlEquation'),
                   model_uri=RHEA.htmlEquation, domain=None, range=Optional[str])

slots.ec = Slot(uri=RHEA.ec, name="ec", curie=RHEA.curie('ec'),
                   model_uri=RHEA.ec, domain=None, range=Optional[Union[str, List[str]]])

slots.compound = Slot(uri=RHEA.compound, name="compound", curie=RHEA.curie('compound'),
                   model_uri=RHEA.compound, domain=None, range=Optional[Union[str, CompoundId]])

slots.location = Slot(uri=RHEA.location, name="location", curie=RHEA.curie('location'),
                   model_uri=RHEA.location, domain=None, range=Optional[Union[str, "LocationEnum"]])

slots.isTransport = Slot(uri=RHEA.isTransport, name="isTransport", curie=RHEA.curie('isTransport'),
                   model_uri=RHEA.isTransport, domain=None, range=Optional[Union[bool, Bool]])

slots.isChemicallyBalanced = Slot(uri=RHEA.isChemicallyBalanced, name="isChemicallyBalanced", curie=RHEA.curie('isChemicallyBalanced'),
                   model_uri=RHEA.isChemicallyBalanced, domain=None, range=Optional[Union[bool, Bool]])

slots.substratesOrProducts = Slot(uri=RHEA.substratesOrProducts, name="substratesOrProducts", curie=RHEA.curie('substratesOrProducts'),
                   model_uri=RHEA.substratesOrProducts, domain=None, range=Optional[Union[Union[str, ReactionSideId], List[Union[str, ReactionSideId]]]])

slots.substrates = Slot(uri=RHEA.substrates, name="substrates", curie=RHEA.curie('substrates'),
                   model_uri=RHEA.substrates, domain=None, range=Optional[Union[str, ReactionSideId]])

slots.products = Slot(uri=RHEA.products, name="products", curie=RHEA.curie('products'),
                   model_uri=RHEA.products, domain=None, range=Optional[Union[str, ReactionSideId]])

slots.side = Slot(uri=RHEA.side, name="side", curie=RHEA.curie('side'),
                   model_uri=RHEA.side, domain=None, range=Optional[Union[Union[str, ReactionSideId], List[Union[str, ReactionSideId]]]])

slots.hasBidirectionalReaction = Slot(uri=RHEA.bidirectionalReaction, name="hasBidirectionalReaction", curie=RHEA.curie('bidirectionalReaction'),
                   model_uri=RHEA.hasBidirectionalReaction, domain=None, range=Optional[Union[str, BidirectionalReactionId]])

slots.hasDirectionalReaction = Slot(uri=RHEA.directionalReaction, name="hasDirectionalReaction", curie=RHEA.curie('directionalReaction'),
                   model_uri=RHEA.hasDirectionalReaction, domain=None, range=Optional[Union[Union[str, DirectionalReactionId], List[Union[str, DirectionalReactionId]]]])

slots.transformableTo = Slot(uri=RHEA.transformableTo, name="transformableTo", curie=RHEA.curie('transformableTo'),
                   model_uri=RHEA.transformableTo, domain=None, range=Optional[Union[str, ReactionSideId]])

slots.curatedOrder = Slot(uri=RHEA.curatedOrder, name="curatedOrder", curie=RHEA.curie('curatedOrder'),
                   model_uri=RHEA.curatedOrder, domain=None, range=Optional[int])

slots.position = Slot(uri=RHEA.position, name="position", curie=RHEA.curie('position'),
                   model_uri=RHEA.position, domain=None, range=Optional[int])

slots.reactivePart = Slot(uri=RHEA.reactivePart, name="reactivePart", curie=RHEA.curie('reactivePart'),
                   model_uri=RHEA.reactivePart, domain=None, range=Optional[Union[str, List[str]]])

slots.underlyingChebi = Slot(uri=RHEA.underlyingChebi, name="underlyingChebi", curie=RHEA.curie('underlyingChebi'),
                   model_uri=RHEA.underlyingChebi, domain=None, range=Optional[Union[str, CHEBIIdentifier]])

slots.polymerizationIndex = Slot(uri=RHEA.polymerizationIndex, name="polymerizationIndex", curie=RHEA.curie('polymerizationIndex'),
                   model_uri=RHEA.polymerizationIndex, domain=None, range=Optional[Union[str, "PolymerizationIndexEnum"]])

slots.contains = Slot(uri=RHEA.contains, name="contains", curie=RHEA.curie('contains'),
                   model_uri=RHEA.contains, domain=None, range=Optional[Union[Union[str, ReactionParticipantId], List[Union[str, ReactionParticipantId]]]])

slots.contains1 = Slot(uri=RHEA.contains1, name="contains1", curie=RHEA.curie('contains1'),
                   model_uri=RHEA.contains1, domain=None, range=Optional[Union[str, List[str]]])

slots.contains2 = Slot(uri=RHEA.contains2, name="contains2", curie=RHEA.curie('contains2'),
                   model_uri=RHEA.contains2, domain=None, range=Optional[Union[str, List[str]]])

slots.contains4 = Slot(uri=RHEA.contains4, name="contains4", curie=RHEA.curie('contains4'),
                   model_uri=RHEA.contains4, domain=None, range=Optional[Union[str, List[str]]])

slots.contains3 = Slot(uri=RHEA.contains3, name="contains3", curie=RHEA.curie('contains3'),
                   model_uri=RHEA.contains3, domain=None, range=Optional[Union[str, List[str]]])

slots.contains6 = Slot(uri=RHEA.contains6, name="contains6", curie=RHEA.curie('contains6'),
                   model_uri=RHEA.contains6, domain=None, range=Optional[Union[str, List[str]]])

slots.contains5 = Slot(uri=RHEA.contains5, name="contains5", curie=RHEA.curie('contains5'),
                   model_uri=RHEA.contains5, domain=None, range=Optional[Union[str, List[str]]])

slots.contains8 = Slot(uri=RHEA.contains8, name="contains8", curie=RHEA.curie('contains8'),
                   model_uri=RHEA.contains8, domain=None, range=Optional[Union[str, List[str]]])

slots.containsN = Slot(uri=RHEA.containsN, name="containsN", curie=RHEA.curie('containsN'),
                   model_uri=RHEA.containsN, domain=None, range=Optional[Union[str, List[str]]])

slots.contains7 = Slot(uri=RHEA.contains7, name="contains7", curie=RHEA.curie('contains7'),
                   model_uri=RHEA.contains7, domain=None, range=Optional[Union[str, List[str]]])

slots.contains16 = Slot(uri=RHEA.contains16, name="contains16", curie=RHEA.curie('contains16'),
                   model_uri=RHEA.contains16, domain=None, range=Optional[Union[str, List[str]]])

slots.contains9 = Slot(uri=RHEA.contains9, name="contains9", curie=RHEA.curie('contains9'),
                   model_uri=RHEA.contains9, domain=None, range=Optional[Union[str, List[str]]])

slots.contains20 = Slot(uri=RHEA.contains20, name="contains20", curie=RHEA.curie('contains20'),
                   model_uri=RHEA.contains20, domain=None, range=Optional[Union[str, List[str]]])

slots.contains11 = Slot(uri=RHEA.contains11, name="contains11", curie=RHEA.curie('contains11'),
                   model_uri=RHEA.contains11, domain=None, range=Optional[Union[str, List[str]]])

slots.contains12 = Slot(uri=RHEA.contains12, name="contains12", curie=RHEA.curie('contains12'),
                   model_uri=RHEA.contains12, domain=None, range=Optional[Union[str, List[str]]])

slots.containsNminus1 = Slot(uri=RHEA.containsNminus1, name="containsNminus1", curie=RHEA.curie('containsNminus1'),
                   model_uri=RHEA.containsNminus1, domain=None, range=Optional[Union[str, List[str]]])

slots.contains2n = Slot(uri=RHEA.contains2n, name="contains2n", curie=RHEA.curie('contains2n'),
                   model_uri=RHEA.contains2n, domain=None, range=Optional[Union[str, List[str]]])

slots.contains10 = Slot(uri=RHEA.contains10, name="contains10", curie=RHEA.curie('contains10'),
                   model_uri=RHEA.contains10, domain=None, range=Optional[Union[str, List[str]]])

slots.contains22 = Slot(uri=RHEA.contains22, name="contains22", curie=RHEA.curie('contains22'),
                   model_uri=RHEA.contains22, domain=None, range=Optional[Union[str, List[str]]])

slots.contains24 = Slot(uri=RHEA.contains24, name="contains24", curie=RHEA.curie('contains24'),
                   model_uri=RHEA.contains24, domain=None, range=Optional[Union[str, List[str]]])

slots.containsNplus1 = Slot(uri=RHEA.containsNplus1, name="containsNplus1", curie=RHEA.curie('containsNplus1'),
                   model_uri=RHEA.containsNplus1, domain=None, range=Optional[Union[str, List[str]]])

slots.contains27 = Slot(uri=RHEA.contains27, name="contains27", curie=RHEA.curie('contains27'),
                   model_uri=RHEA.contains27, domain=None, range=Optional[Union[str, List[str]]])

slots.contains18 = Slot(uri=RHEA.contains18, name="contains18", curie=RHEA.curie('contains18'),
                   model_uri=RHEA.contains18, domain=None, range=Optional[Union[str, List[str]]])

slots.contains28 = Slot(uri=RHEA.contains28, name="contains28", curie=RHEA.curie('contains28'),
                   model_uri=RHEA.contains28, domain=None, range=Optional[Union[str, List[str]]])

slots.contains32 = Slot(uri=RHEA.contains32, name="contains32", curie=RHEA.curie('contains32'),
                   model_uri=RHEA.contains32, domain=None, range=Optional[Union[str, List[str]]])

slots.contains17 = Slot(uri=RHEA.contains17, name="contains17", curie=RHEA.curie('contains17'),
                   model_uri=RHEA.contains17, domain=None, range=Optional[Union[str, List[str]]])

slots.contains13 = Slot(uri=RHEA.contains13, name="contains13", curie=RHEA.curie('contains13'),
                   model_uri=RHEA.contains13, domain=None, range=Optional[Union[str, List[str]]])

slots.contains14 = Slot(uri=RHEA.contains14, name="contains14", curie=RHEA.curie('contains14'),
                   model_uri=RHEA.contains14, domain=None, range=Optional[Union[str, List[str]]])

slots.contains40 = Slot(uri=RHEA.contains40, name="contains40", curie=RHEA.curie('contains40'),
                   model_uri=RHEA.contains40, domain=None, range=Optional[Union[str, List[str]]])

slots.contains26 = Slot(uri=RHEA.contains26, name="contains26", curie=RHEA.curie('contains26'),
                   model_uri=RHEA.contains26, domain=None, range=Optional[Union[str, List[str]]])

slots.contains21 = Slot(uri=RHEA.contains21, name="contains21", curie=RHEA.curie('contains21'),
                   model_uri=RHEA.contains21, domain=None, range=Optional[Union[str, List[str]]])

slots.contains19 = Slot(uri=RHEA.contains19, name="contains19", curie=RHEA.curie('contains19'),
                   model_uri=RHEA.contains19, domain=None, range=Optional[Union[str, List[str]]])

slots.AbstractReaction_ec = Slot(uri=RHEA.ec, name="AbstractReaction_ec", curie=RHEA.curie('ec'),
                   model_uri=RHEA.AbstractReaction_ec, domain=AbstractReaction, range=Optional[Union[str, List[str]]])

slots.AbstractReaction_subClassOf = Slot(uri=RDFS.subClassOf, name="AbstractReaction_subClassOf", curie=RDFS.curie('subClassOf'),
                   model_uri=RHEA.AbstractReaction_subClassOf, domain=AbstractReaction, range=Optional[Union[str, AbstractReactionId]])

slots.Reaction_subClassOf = Slot(uri=RDFS.subClassOf, name="Reaction_subClassOf", curie=RDFS.curie('subClassOf'),
                   model_uri=RHEA.Reaction_subClassOf, domain=Reaction, range=Optional[Union[str, ReactionId]])

slots.DirectionalReaction_subClassOf = Slot(uri=RDFS.subClassOf, name="DirectionalReaction_subClassOf", curie=RDFS.curie('subClassOf'),
                   model_uri=RHEA.DirectionalReaction_subClassOf, domain=DirectionalReaction, range=Optional[Union[str, DirectionalReactionId]])

slots.BidirectionalReaction_subClassOf = Slot(uri=RDFS.subClassOf, name="BidirectionalReaction_subClassOf", curie=RDFS.curie('subClassOf'),
                   model_uri=RHEA.BidirectionalReaction_subClassOf, domain=BidirectionalReaction, range=Optional[Union[str, BidirectionalReactionId]])

slots.ReactionParticipant_subClassOf = Slot(uri=RDFS.subClassOf, name="ReactionParticipant_subClassOf", curie=RDFS.curie('subClassOf'),
                   model_uri=RHEA.ReactionParticipant_subClassOf, domain=ReactionParticipant, range=Optional[Union[str, CompoundId]])

slots.ReactivePart_subClassOf = Slot(uri=RDFS.subClassOf, name="ReactivePart_subClassOf", curie=RDFS.curie('subClassOf'),
                   model_uri=RHEA.ReactivePart_subClassOf, domain=ReactivePart, range=Optional[Union[str, CompoundId]])

slots.Compound_subClassOf = Slot(uri=RDFS.subClassOf, name="Compound_subClassOf", curie=RDFS.curie('subClassOf'),
                   model_uri=RHEA.Compound_subClassOf, domain=Compound, range=Optional[Union[str, CompoundId]])

slots.SmallMolecule_subClassOf = Slot(uri=RDFS.subClassOf, name="SmallMolecule_subClassOf", curie=RDFS.curie('subClassOf'),
                   model_uri=RHEA.SmallMolecule_subClassOf, domain=SmallMolecule, range=Optional[Union[str, SmallMoleculeId]])