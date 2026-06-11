# ADMBw Knowledge: Konnektor-Regeln & Viewpoint-Übersicht

> **OpenWebUI Knowledge-Datei.** Enthält alle EA-Metatypen + erlaubte Stereotype, sowie die vollständige Viewpoint-Liste.
> Bei Fragen zu Beziehungstypen oder Viewpoint-Zuordnung: hier semantisch suchen.

## Goldene Regel

Jede Beziehung = EA-Metatyp + Stereotyp. Der Stereotyp MUSS auf diesen Metatyp anwendbar sein (siehe Knowledge: Stereotypes).

## EA-Metatypen & Häufigste Stereotype

| EA-Metatyp | Häufigste Stereotype |
|-----------|---------------------|
| **Dependency** (100) | `AchievedEffect`, `ActivityPerformableUnderCondition`, `ActsUpon`, `ActualConditionToActualResource`, `ActualMeasurementSetAppliesFor` +95 |
| **Class** (70) | `Architecture`, `Asset`, `Capability`, `CapabilityConfiguration`, `Classification` +65 |
| **Object** (21) | `Achiever`, `ActualCondition`, `ActualEnduringTask`, `ActualEnterprisePhase`, `ActualEnvironment` +16 |
| **Part** (20) | `AssetRole`, `CapabilityRole`, `ConceptRole`, `DataRole`, `InformationRole` +15 |
| **Abstraction** (10) | `CapabilityForTask`, `Consumes`, `Exhibits`, `Implements`, `IsCapableToPerform` +5 |
| **Activity** (7) | `BusinessProcess`, `Function`, `OperationalActivity`, `OperationalActivityAction`, `SecurityProcess` +2 |
| **Slot** (6) | `ActualMeasurement`, `ActualOrganizationRole`, `ActualProjectMilestoneRole`, `ActualResourceRole`, `ActualServiceSpecificationRole` +1 |
| **InformationFlow** (6) | `ActualResourceRelationship`, `Command`, `Control`, `OperationalExchange`, `ResourceExchange` +1 |
| **Note** (5) | `Alias`, `ArchitectureMetadata`, `Definition`, `Information`, `Metadata` |
| **Realisation** (4) | `ActivitySupportsService`, `Evaluates`, `RealiseRequirement`, `RealizesRecommendation` |
| **Generalization** (4) | `CapabilityGeneralization`, `ProcessGeneralization`, `PropertySetGeneralization`, `ServiceSpecificationGeneralization` |
| **Message** (4) | `InteractionMessage`, `OperationalMessage`, `ResourceMessage`, `ServiceMessage` |
| **Package** (3) | `ArchitecturalDescription`, `DataModel`, `ElementCatalogue` |
| **Requirement** (3) | `BWRequirement`, `FunctionalRequirement`, `NonfunctionalRequirement` |
| **DataType** (3) | `Condition`, `GeoPoliticalExtentType`, `Location` |
| **Action** (3) | `FunctionAction`, `OperationalActivityAction`, `ServiceFunctionAction` |
| **ControlFlow** (3) | `FunctionControlFlow`, `OperationalControlFlow`, `OperationalMessageFlow` |
| **Operation** (3) | `OperationalMethod`, `ResourceMethod`, `ServiceMethod` |
| **Parameter** (3) | `OperationalParameter`, `ResourceParameter`, `ServiceParameter` |
| **Port** (3) | `OperationalPort`, `ResourcePort`, `ServicePort` |
| **StateMachine** (3) | `ResourceStateDescription`, `ServiceStateDescription`, `StateDescription` |
| **ObjectFlow** (2) | `FunctionObjectFlow`, `OperationalObjectFlow` |
| **Connector** (2) | `OperationalConnector`, `ResourceConnector` |
| **Signal** (2) | `OperationalSignal`, `ResourceSignal` |
| **Aggregation** (2) | `PartOfCatalogue`, `PartOfCategory` |
| **Constraint** (2) | `Rule`, `SecurityConstraint` |

## Vollständige Viewpoint-Liste (53 Viewpoints, 6 Kategorien)

### 🏛️ Concept Viewpoints (C)
| Kürzel | Name | Fokus |
|--------|------|-------|
| C1 | Capability Taxonomy | Fähigkeiten, Taxonomie, Messbarkeit |
| C2 | Enterprise Vision | Strategischer Kontext, Vision, Enduring Tasks |
| C3 | Capability Dependencies | Abhängigkeiten zwischen Fähigkeiten |
| C4 | Standard Processes | Standardisierte Prozesse |
| C5 | Effects | Wirkungen, Effekte |
| C7 | Performance Parameters | Leistungsparameter |
| C8 | Planning Assumptions | Planungsannahmen |
| Cr | Capability Roadmap | Zeitliche Fähigkeitsentwicklung |

### 🔌 Service Specification Viewpoints (S)
| Kürzel | Name | Fokus |
|--------|------|-------|
| S1 | Service Taxonomy | Service-Taxonomie |
| S2 | Service Structure | Service-Struktur |
| S3 | Service Interfaces | Service-Schnittstellen |
| S4 | Service Functions | Service-Funktionen |
| S5 | Service States | Service-Zustände |
| S6 | Service Interactions | Service-Interaktionen |
| S7 | Service Interface Parameters | Schnittstellenparameter |
| S8 | Service Policy | Service-Richtlinien |
| Sr | Service Roadmap | Service-Roadmap |
| C1-S1 | Capability to Service Mapping | Fähigkeit→Service |

### 🧠 Logical Specification Viewpoints (L)
| Kürzel | Name | Fokus |
|--------|------|-------|
| L1 | Node Types | Knotentypen (OperationalAgent, OpNode) |
| L2 | Logical Scenario | Szenarien, High-Level Operational Concept |
| L3 | Node Interactions | Knoteninteraktionen, Needlines, Informationsflüsse |
| L4 | Logical Activities | Aktivitäten, Prozesse, OperationalActivity |
| L5 | Logical States | Zustandsautomaten |
| L6 | Logical Sequence | Sequenzen, Event-Traces |
| L7 | Information Model | Informationsmodell, InformationElements |
| L8 | Logical Constraints | Regeln, OperationalConstraints |
| Lr | Lines of Development | Entwicklungslinien |
| L2-L3 | Logical Concept | Kombinierte Szenario+Interaktion |

### 🖥️ Physical Resource Viewpoints (P)
| Kürzel | Name | Fokus |
|--------|------|-------|
| P1 | Resource Types | Ressourcentypen (System, Software, Organization…) |
| P2 | Resource Structure | Ressourcenstruktur (Komposition) |
| P3 | Resource Connectivity | Ressourcenkonnektivität, Netzwerke, Protokolle |
| P4 | Resource Functions | Ressourcenfunktionen |
| P5 | Resource States | Ressourcenzustände |
| P6 | Resource Sequence | Ressourcen-Sequenzen |
| P7 | Data Model | Datenmodell |
| P8 | Resource Constraints | Ressourcen-Constraints |
| Pr | Configuration Management | Konfigurationsmanagement |
| L4-P4 | Activity to Function Mapping | Aktivität→Funktion |

### 📐 Architecture Foundation (A)
| Kürzel | Name | Fokus |
|--------|------|-------|
| A1 | Meta-Data Definitions | Metadaten |
| A2 | Architecture Products | Architekturprodukte |
| A3 | Architecture Correspondence | Korrespondenzregeln |
| A4 | Methodology Used | Methodik |
| A5 | Architecture Status | Status |
| A6 | Architecture Versions | Versionierung |
| A7 | Architecture Compliance | Compliance |
| A8 | Standards | Standards, Protokolle |
| Ar | Architecture Roadmap | Architektur-Roadmap |

### 📋 Requirement Viewpoints (R)
| Kürzel | Name | Fokus |
|--------|------|-------|
| R2 | Requirement Catalogue | Anforderungskatalog |
| R3 | Requirement Dependencies | Anforderungsabhängigkeiten |
| R7 | Requirement Derivation | Anforderungsableitung |
| R8 | Requirement Fulfilment | Anforderungserfüllung |
| Rr | Requirement Realization | Anforderungsumsetzung |
