

CREATE TABLE "Class" (
	comment TEXT, 
	type TEXT, 
	label TEXT, 
	PRIMARY KEY (comment, type, label)
);

CREATE TABLE "Compound" (
	type TEXT, 
	comment TEXT, 
	label TEXT, 
	PRIMARY KEY (type, comment, label)
);

CREATE TABLE "DirectionalReaction" (
	"bidirectionalReaction" INTEGER, 
	"isTransport" BOOLEAN, 
	type TEXT, 
	"isChemicallyBalanced" BOOLEAN, 
	substrates TEXT, 
	"htmlEquation" TEXT, 
	accession TEXT, 
	citation INTEGER, 
	equation TEXT, 
	status VARCHAR(11), 
	products TEXT, 
	label TEXT, 
	"subClassOf" TEXT, 
	"seeAlso" TEXT, 
	comment TEXT, 
	ec TEXT, 
	PRIMARY KEY ("bidirectionalReaction", "isTransport", type, "isChemicallyBalanced", substrates, "htmlEquation", accession, citation, equation, status, products, label, "subClassOf", "seeAlso", comment, ec)
);

CREATE TABLE "GenericCompound" (
	label TEXT, 
	type TEXT, 
	comment TEXT, 
	PRIMARY KEY (label, type, comment)
);

CREATE TABLE "GenericPolynucleotide" (
	label TEXT, 
	comment TEXT, 
	name TEXT, 
	type TEXT, 
	"reactivePart" TEXT, 
	accession TEXT, 
	"htmlName" TEXT, 
	PRIMARY KEY (label, comment, name, type, "reactivePart", accession, "htmlName")
);

CREATE TABLE "GenericPolypeptide" (
	label TEXT, 
	comment TEXT, 
	"reactivePart" TEXT, 
	name TEXT, 
	type TEXT, 
	accession TEXT, 
	"htmlName" TEXT, 
	PRIMARY KEY (label, comment, "reactivePart", name, type, accession, "htmlName")
);

CREATE TABLE "Location" (
	type TEXT, 
	PRIMARY KEY (type)
);

CREATE TABLE "Polymer" (
	comment TEXT, 
	label TEXT, 
	type TEXT, 
	charge INTEGER, 
	"underlyingChebi" TEXT, 
	formula TEXT, 
	accession TEXT, 
	"htmlName" TEXT, 
	name TEXT, 
	"polymerizationIndex" VARCHAR(3), 
	PRIMARY KEY (comment, label, type, charge, "underlyingChebi", formula, accession, "htmlName", name, "polymerizationIndex")
);

CREATE TABLE "Property" (
	type TEXT, 
	PRIMARY KEY (type)
);

CREATE TABLE "Reaction" (
	status VARCHAR(11), 
	accession TEXT, 
	"isTransport" BOOLEAN, 
	"bidirectionalReaction" INTEGER, 
	"isChemicallyBalanced" BOOLEAN, 
	citation INTEGER, 
	type TEXT, 
	"directionalReaction" INTEGER, 
	"htmlEquation" TEXT, 
	equation TEXT, 
	side TEXT, 
	label TEXT, 
	comment TEXT, 
	"subClassOf" TEXT, 
	ec TEXT, 
	"seeAlso" TEXT, 
	PRIMARY KEY (status, accession, "isTransport", "bidirectionalReaction", "isChemicallyBalanced", citation, type, "directionalReaction", "htmlEquation", equation, side, label, comment, "subClassOf", ec, "seeAlso")
);

CREATE TABLE "ReactionParticipant" (
	"subClassOf" TEXT, 
	compound TEXT, 
	type TEXT, 
	location VARCHAR(3), 
	PRIMARY KEY ("subClassOf", compound, type, location)
);

CREATE TABLE "ReactionSide" (
	contains TEXT, 
	"transformableTo" TEXT, 
	type TEXT, 
	"curatedOrder" INTEGER, 
	contains1 TEXT, 
	contains2 TEXT, 
	contains4 TEXT, 
	contains3 TEXT, 
	contains6 TEXT, 
	contains5 TEXT, 
	contains8 TEXT, 
	"containsN" TEXT, 
	contains7 TEXT, 
	contains16 TEXT, 
	contains9 TEXT, 
	contains20 TEXT, 
	contains11 TEXT, 
	contains12 TEXT, 
	"containsNminus1" TEXT, 
	contains2n TEXT, 
	contains10 TEXT, 
	contains22 TEXT, 
	contains24 TEXT, 
	"containsNplus1" TEXT, 
	contains27 TEXT, 
	contains18 TEXT, 
	contains28 TEXT, 
	contains32 TEXT, 
	contains17 TEXT, 
	contains13 TEXT, 
	contains14 TEXT, 
	contains40 TEXT, 
	contains26 TEXT, 
	contains21 TEXT, 
	contains19 TEXT, 
	PRIMARY KEY (contains, "transformableTo", type, "curatedOrder", contains1, contains2, contains4, contains3, contains6, contains5, contains8, "containsN", contains7, contains16, contains9, contains20, contains11, contains12, "containsNminus1", contains2n, contains10, contains22, contains24, "containsNplus1", contains27, contains18, contains28, contains32, contains17, contains13, contains14, contains40, contains26, contains21, contains19)
);

CREATE TABLE "ReactivePart" (
	type TEXT, 
	name TEXT, 
	charge INTEGER, 
	"subClassOf" TEXT, 
	chebi TEXT, 
	formula TEXT, 
	"htmlName" TEXT, 
	position TEXT, 
	PRIMARY KEY (type, name, charge, "subClassOf", chebi, formula, "htmlName", position)
);

CREATE TABLE "SmallMolecule" (
	comment TEXT, 
	label TEXT, 
	type TEXT, 
	chebi TEXT, 
	"htmlName" TEXT, 
	accession TEXT, 
	formula TEXT, 
	charge INTEGER, 
	"subClassOf" TEXT, 
	name TEXT, 
	PRIMARY KEY (comment, label, type, chebi, "htmlName", accession, formula, charge, "subClassOf", name)
);

CREATE TABLE "BidirectionalReaction_id" (
	backref_id TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(backref_id) REFERENCES "BidirectionalReaction_id" (id)
);

CREATE TABLE "Class_id" (
	backref_id TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(backref_id) REFERENCES "Class_id" (id)
);

CREATE TABLE "Compound_id" (
	backref_id TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(backref_id) REFERENCES "Compound_id" (id)
);

CREATE TABLE "DirectionalReaction_id" (
	backref_id TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(backref_id) REFERENCES "DirectionalReaction_id" (id)
);

CREATE TABLE "GenericCompound_id" (
	backref_id TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(backref_id) REFERENCES "GenericCompound_id" (id)
);

CREATE TABLE "GenericPolynucleotide_id" (
	backref_id TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(backref_id) REFERENCES "GenericPolynucleotide_id" (id)
);

CREATE TABLE "GenericPolypeptide_id" (
	backref_id TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(backref_id) REFERENCES "GenericPolypeptide_id" (id)
);

CREATE TABLE "Location_id" (
	backref_id TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(backref_id) REFERENCES "Location_id" (id)
);

CREATE TABLE "Polymer_id" (
	backref_id TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(backref_id) REFERENCES "Polymer_id" (id)
);

CREATE TABLE "Property_id" (
	backref_id TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(backref_id) REFERENCES "Property_id" (id)
);

CREATE TABLE "Reaction_id" (
	backref_id TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(backref_id) REFERENCES "Reaction_id" (id)
);

CREATE TABLE "ReactionParticipant_id" (
	backref_id TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(backref_id) REFERENCES "ReactionParticipant_id" (id)
);

CREATE TABLE "ReactionSide_id" (
	backref_id TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(backref_id) REFERENCES "ReactionSide_id" (id)
);

CREATE TABLE "ReactivePart_id" (
	backref_id TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(backref_id) REFERENCES "ReactivePart_id" (id)
);

CREATE TABLE "SmallMolecule_id" (
	backref_id TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(backref_id) REFERENCES "SmallMolecule_id" (id)
);

CREATE TABLE "BidirectionalReaction" (
	"bidirectionalReaction" INTEGER, 
	"seeAlso" TEXT, 
	citation INTEGER, 
	label TEXT, 
	accession TEXT, 
	equation TEXT, 
	status VARCHAR(11), 
	"isTransport" BOOLEAN, 
	"substratesOrProducts" TEXT, 
	type TEXT, 
	"isChemicallyBalanced" BOOLEAN, 
	"htmlEquation" TEXT, 
	"subClassOf" TEXT, 
	comment TEXT, 
	ec TEXT, 
	PRIMARY KEY ("bidirectionalReaction", "seeAlso", citation, label, accession, equation, status, "isTransport", "substratesOrProducts", type, "isChemicallyBalanced", "htmlEquation", "subClassOf", comment, ec), 
	FOREIGN KEY("subClassOf") REFERENCES "Class_id" (id)
);

CREATE TABLE "BidirectionalReaction_directionalReaction" (
	backref_id TEXT, 
	"directionalReaction" INTEGER, 
	PRIMARY KEY (backref_id, "directionalReaction"), 
	FOREIGN KEY(backref_id) REFERENCES "BidirectionalReaction_id" (id)
);

CREATE TABLE "BidirectionalReaction_side" (
	backref_id TEXT, 
	side TEXT, 
	PRIMARY KEY (backref_id, side), 
	FOREIGN KEY(backref_id) REFERENCES "BidirectionalReaction_id" (id)
);

CREATE TABLE "DirectionalReaction_directionalReaction" (
	backref_id TEXT, 
	"directionalReaction" INTEGER, 
	PRIMARY KEY (backref_id, "directionalReaction"), 
	FOREIGN KEY(backref_id) REFERENCES "DirectionalReaction_id" (id)
);

CREATE TABLE "DirectionalReaction_side" (
	backref_id TEXT, 
	side TEXT, 
	PRIMARY KEY (backref_id, side), 
	FOREIGN KEY(backref_id) REFERENCES "DirectionalReaction_id" (id)
);
