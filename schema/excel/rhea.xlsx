

CREATE TABLE "BidirectionalReaction" (
	comment TEXT, 
	type TEXT, 
	label TEXT, 
	status VARCHAR(11), 
	accession TEXT, 
	"seeAlso" TEXT, 
	"isTransport" BOOLEAN, 
	"isChemicallyBalanced" BOOLEAN, 
	citation INTEGER, 
	"htmlEquation" TEXT, 
	equation TEXT, 
	ec TEXT, 
	"substratesOrProducts" TEXT, 
	"subClassOf" TEXT, 
	PRIMARY KEY (comment, type, label, status, accession, "seeAlso", "isTransport", "isChemicallyBalanced", citation, "htmlEquation", equation, ec, "substratesOrProducts", "subClassOf")
);

CREATE TABLE "Class" (
	comment TEXT, 
	type TEXT, 
	label TEXT, 
	PRIMARY KEY (comment, type, label)
);

CREATE TABLE "Compound" (
	comment TEXT, 
	type TEXT, 
	label TEXT, 
	name TEXT, 
	accession TEXT, 
	"htmlName" TEXT, 
	formula TEXT, 
	"subClassOf" TEXT, 
	PRIMARY KEY (comment, type, label, name, accession, "htmlName", formula, "subClassOf")
);

CREATE TABLE "GenericCompound" (
	comment TEXT, 
	type TEXT, 
	label TEXT, 
	name TEXT, 
	accession TEXT, 
	"htmlName" TEXT, 
	formula TEXT, 
	"subClassOf" TEXT, 
	"reactivePart" TEXT, 
	PRIMARY KEY (comment, type, label, name, accession, "htmlName", formula, "subClassOf", "reactivePart")
);

CREATE TABLE "GenericPolynucleotide" (
	comment TEXT, 
	type TEXT, 
	label TEXT, 
	name TEXT, 
	accession TEXT, 
	"htmlName" TEXT, 
	formula TEXT, 
	"subClassOf" TEXT, 
	"reactivePart" TEXT, 
	PRIMARY KEY (comment, type, label, name, accession, "htmlName", formula, "subClassOf", "reactivePart")
);

CREATE TABLE "GenericPolypeptide" (
	comment TEXT, 
	type TEXT, 
	label TEXT, 
	name TEXT, 
	accession TEXT, 
	"htmlName" TEXT, 
	formula TEXT, 
	"subClassOf" TEXT, 
	"reactivePart" TEXT, 
	PRIMARY KEY (comment, type, label, name, accession, "htmlName", formula, "subClassOf", "reactivePart")
);

CREATE TABLE "Polymer" (
	comment TEXT, 
	type TEXT, 
	label TEXT, 
	name TEXT, 
	accession TEXT, 
	"htmlName" TEXT, 
	formula TEXT, 
	"subClassOf" TEXT, 
	charge INTEGER, 
	"underlyingChebi" TEXT, 
	"polymerizationIndex" VARCHAR(3), 
	PRIMARY KEY (comment, type, label, name, accession, "htmlName", formula, "subClassOf", charge, "underlyingChebi", "polymerizationIndex")
);

CREATE TABLE "Reaction" (
	comment TEXT, 
	type TEXT, 
	label TEXT, 
	status VARCHAR(11), 
	accession TEXT, 
	"seeAlso" TEXT, 
	"isTransport" BOOLEAN, 
	"isChemicallyBalanced" BOOLEAN, 
	citation INTEGER, 
	"htmlEquation" TEXT, 
	equation TEXT, 
	"hasDirectionalReaction" TEXT, 
	"hasBidirectionalReaction" TEXT, 
	side TEXT, 
	ec TEXT, 
	"subClassOf" TEXT, 
	PRIMARY KEY (comment, type, label, status, accession, "seeAlso", "isTransport", "isChemicallyBalanced", citation, "htmlEquation", equation, "hasDirectionalReaction", "hasBidirectionalReaction", side, ec, "subClassOf")
);

CREATE TABLE "ReactionParticipant" (
	comment TEXT, 
	type TEXT, 
	label TEXT, 
	compound TEXT, 
	location VARCHAR(3), 
	"subClassOf" TEXT, 
	PRIMARY KEY (comment, type, label, compound, location, "subClassOf")
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
	comment TEXT, 
	type TEXT, 
	label TEXT, 
	name TEXT, 
	charge INTEGER, 
	chebi TEXT, 
	formula TEXT, 
	"htmlName" TEXT, 
	position INTEGER, 
	"subClassOf" TEXT, 
	PRIMARY KEY (comment, type, label, name, charge, chebi, formula, "htmlName", position, "subClassOf")
);

CREATE TABLE "SmallMolecule" (
	comment TEXT, 
	type TEXT, 
	label TEXT, 
	accession TEXT, 
	formula TEXT, 
	chebi TEXT, 
	"htmlName" TEXT, 
	charge INTEGER, 
	name TEXT, 
	"subClassOf" TEXT, 
	PRIMARY KEY (comment, type, label, accession, formula, chebi, "htmlName", charge, name, "subClassOf")
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

CREATE TABLE "Polymer_id" (
	backref_id TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(backref_id) REFERENCES "Polymer_id" (id)
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

CREATE TABLE "DirectionalReaction" (
	comment TEXT, 
	type TEXT, 
	label TEXT, 
	status VARCHAR(11), 
	accession TEXT, 
	"seeAlso" TEXT, 
	"isTransport" BOOLEAN, 
	"isChemicallyBalanced" BOOLEAN, 
	citation INTEGER, 
	"htmlEquation" TEXT, 
	equation TEXT, 
	ec TEXT, 
	substrates TEXT, 
	products TEXT, 
	"subClassOf" TEXT, 
	PRIMARY KEY (comment, type, label, status, accession, "seeAlso", "isTransport", "isChemicallyBalanced", citation, "htmlEquation", equation, ec, substrates, products, "subClassOf"), 
	FOREIGN KEY(substrates) REFERENCES "ReactionSide_id" (id), 
	FOREIGN KEY(products) REFERENCES "ReactionSide_id" (id)
);
