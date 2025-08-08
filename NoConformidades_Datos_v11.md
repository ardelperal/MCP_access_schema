# Estructura de la Base de Datos y Relaciones

Este documento detalla la estructura de la base de datos de Access, incluyendo sus tablas, columnas y relaciones. Las relaciones se obtuvieron directamente del esquema de la base de datos.

## Estructura de Tablas

### Tablas Locales

#### Tabla: `Copia de TbNCARAvisos`
| Nombre de Columna | Tipo de Dato |
|-------------------|--------------|
| `Fecha` | `Date` |
| `ID` | `Integer` |
| `IDAR` | `Integer` |
| `IDCorreo0` | `Integer` |
| `IDCorreo15` | `Integer` |
| `IDCorreo7` | `Integer` |

#### Tabla: `TbAnexos`
| Nombre de Columna | Tipo de Dato |
|-------------------|--------------|
| `DescripcionAnexo` | `Text (Long)` |
| `FechaAnexo` | `Date` |
| `IDAnexo` | `Integer` |
| `IDNoConformidad` | `Integer` |
| `NombreArchivoFinalAnexo` | `Text` |
| `TituloAnexo` | `Text` |
| `URLInicial` | `Text` |

#### Tabla: `TbAnexosAuditoria`
| Nombre de Columna | Tipo de Dato |
|-------------------|--------------|
| `FechaAnexo` | `Date` |
| `IDAnexo` | `Integer` |
| `IDAuditoria` | `Integer` |
| `NombreArchivo` | `Text` |
| `URLInicial` | `Text` |

#### Tabla: `TbAnexosNCAuditorias`
| Nombre de Columna | Tipo de Dato |
|-------------------|--------------|
| `FechaAnexo` | `Date` |
| `IDAnexo` | `Integer` |
| `IDNoConformidad` | `Integer` |
| `NombreArchivo` | `Text` |
| `URLInicial` | `Text` |

#### Tabla: `TbAuditoriaLog`
| Nombre de Columna | Tipo de Dato |
|-------------------|--------------|
| `Fecha` | `Date` |
| `IDAC` | `Integer` |
| `IDAR` | `Integer` |
| `IDLog` | `Integer` |
| `IDNC` | `Integer` |
| `Linea` | `Text (Long)` |
| `Titulo` | `Text (Long)` |
| `Usuario` | `Text` |

#### Tabla: `TbAuditorias`
| Nombre de Columna | Tipo de Dato |
|-------------------|--------------|
| `FechaFin` | `Date` |
| `FechaInicio` | `Date` |
| `IDAuditoria` | `Integer` |
| `Tipo` | `Text` |

#### Tabla: `TbAuxPuntoNorma`
| Nombre de Columna | Tipo de Dato |
|-------------------|--------------|
| `PuntoNorma` | `Text` |

#### Tabla: `TbConexiones`
| Nombre de Columna | Tipo de Dato |
|-------------------|--------------|
| `Exitoso` | `Text` |
| `InstaladoFW3` | `Text` |
| `InstaladoFW4` | `Text` |
| `UltimaConexion` | `Date` |
| `UltimaDesconexion` | `Date` |
| `Usuario` | `Text` |

#### Tabla: `TbConsultasPorFechas`
| Nombre de Columna | Tipo de Dato |
|-------------------|--------------|
| `Descripcion` | `Text` |

#### Tabla: `TbDocumentosAuditorias`
| Nombre de Columna | Tipo de Dato |
|-------------------|--------------|
| `Documento` | `Text` |
| `IDAccionRealizada` | `Integer` |
| `IDAuditoria` | `Integer` |
| `IDAuditoriaResultante` | `Integer` |
| `IDDocumento` | `Integer` |
| `IDNoConformidad` | `Integer` |
| `NombreAnexo` | `Text` |

#### Tabla: `TbHerramientaDocAyuda`
| Nombre de Columna | Tipo de Dato |
|-------------------|--------------|
| `NombreArchivoAyuda` | `Text` |
| `NombreFormulario` | `Text` |

#### Tabla: `TbLog`
| Nombre de Columna | Tipo de Dato |
|-------------------|--------------|
| `Fecha` | `Date` |
| `IDAC` | `Integer` |
| `IDAR` | `Integer` |
| `IDLog` | `Integer` |
| `IDNC` | `Integer` |
| `Linea` | `Text (Long)` |
| `Titulo` | `Text (Long)` |
| `Usuario` | `Text` |

#### Tabla: `TbLogAuditoria`
| Nombre de Columna | Tipo de Dato |
|-------------------|--------------|
| `Fecha` | `Date` |
| `IDAC` | `Integer` |
| `IDAR` | `Integer` |
| `IDLog` | `Integer` |
| `IDNC` | `Integer` |
| `Linea` | `Text (Long)` |
| `Titulo` | `Text (Long)` |
| `Usuario` | `Text` |

#### Tabla: `TbNCARAvisos`
| Nombre de Columna | Tipo de Dato |
|-------------------|--------------|
| `Fecha` | `Date` |
| `ID` | `Integer` |
| `IDAR` | `Integer` |
| `IDCorreo0` | `Integer` |
| `IDCorreo15` | `Integer` |
| `IDCorreo7` | `Integer` |

#### Tabla: `TbNCAccionCorrectivas`
| Nombre de Columna | Tipo de Dato |
|-------------------|--------------|
| `AccionCorrectiva` | `Text (Long)` |
| `ESTADO` | `Text` |
| `FechaAccionCorrectiva` | `Date` |
| `FechaFinPrevistaUltima` | `Date` |
| `FechaFinalUltima` | `Date` |
| `FechaInicialMinima` | `Date` |
| `IDAccionCorrectiva` | `Integer` |
| `IDNoConformidad` | `Integer` |
| `NAccion` | `Integer` |
| `Notas` | `Text (Long)` |
| `Responsable` | `Text` |

#### Tabla: `TbNCAccionesRealizadas`
| Nombre de Columna | Tipo de Dato |
|-------------------|--------------|
| `AccionRealizada` | `Text (Long)` |
| `ESTADO` | `Text` |
| `FechaAccionRealizada` | `Date` |
| `FechaFinPrevista` | `Date` |
| `FechaFinReal` | `Date` |
| `FechaInicio` | `Date` |
| `IDAccionCorrectiva` | `Integer` |
| `IDAccionRealizada` | `Integer` |
| `NAccion` | `Integer` |
| `Notas` | `Text (Long)` |
| `Responsable` | `Text` |

#### Tabla: `TbNCAuditoriaAccionCorrectivas`
| Nombre de Columna | Tipo de Dato |
|-------------------|--------------|
| `AccionCorrectiva` | `Text (Long)` |
| `ESTADO` | `Text` |
| `FechaAccionCorrectiva` | `Date` |
| `FechaFinPrevistaUltima` | `Date` |
| `FechaFinalUltima` | `Date` |
| `FechaInicialMinima` | `Date` |
| `ID` | `Integer` |
| `IDAccionCorrectiva` | `Integer` |
| `NAccion` | `Integer` |
| `Notas` | `Text (Long)` |
| `Responsable` | `Text` |

#### Tabla: `TbNCAuditoriaAccionesRealizadas`
| Nombre de Columna | Tipo de Dato |
|-------------------|--------------|
| `AccionRealizada` | `Text (Long)` |
| `ESTADO` | `Text` |
| `FechaAccionRealizada` | `Date` |
| `FechaFinPrevista` | `Date` |
| `FechaFinReal` | `Date` |
| `FechaInicio` | `Date` |
| `IDAccionCorrectiva` | `Integer` |
| `IDAccionRealizada` | `Integer` |
| `NAccion` | `Integer` |
| `Notas` | `Text (Long)` |
| `Responsable` | `Text` |

#### Tabla: `TbNCDocumentos`
| Nombre de Columna | Tipo de Dato |
|-------------------|--------------|
| `Documento` | `Text` |
| `IDAccionRealizada` | `Integer` |
| `IDDocumento` | `Integer` |
| `IDNoConformidad` | `Integer` |
| `IDNoConformidadResultante` | `Integer` |
| `NombreAnexo` | `Text` |

#### Tabla: `TbNCInformacionRAC`
| Nombre de Columna | Tipo de Dato |
|-------------------|--------------|
| `FechaCreacion` | `Date` |
| `FechaEdicion` | `Date` |
| `FechaInformacion` | `Date` |
| `IDInformacionRAC` | `Integer` |
| `IDNoConformidad` | `Integer` |
| `Informacion` | `Text (Long)` |
| `UltimoUsuarioEdita` | `Text` |
| `UsuarioCrea` | `Text` |

#### Tabla: `TbNCInformacionRACAnexos`
| Nombre de Columna | Tipo de Dato |
|-------------------|--------------|
| `FechaAnexo` | `Date` |
| `IDAnexoInformacionRAC` | `Integer` |
| `IDInformacionRAC` | `Integer` |
| `NombreArchivo` | `Text` |

#### Tabla: `TbNoConformidades`
| Nombre de Columna | Tipo de Dato |
|-------------------|--------------|
| `ACR` | `Text (Long)` |
| `Borrado` | `Boolean` |
| `CAUSA` | `Text (Long)` |
| `CausaYAnalisRaiz` | `Text (Long)` |
| `Cerrada` | `Text` |
| `CodConcesionAsociada` | `Text` |
| `CodExp` | `Text` |
| `CodigoNoConformidad` | `Text` |
| `CodigoNoConformidadAsociada` | `Text` |
| `CodigoRiesgo` | `Text` |
| `ConformeControlEficacia` | `Text` |
| `ControlEficacia` | `Text (Long)` |
| `DESCRIPCION` | `Text (Long)` |
| `DetectadoPor` | `Text` |
| `ENTIDADRESPONSABLE` | `Text` |
| `ESTADO` | `Text` |
| `EXPEDIENTE` | `Text` |
| `EsNoConformidad` | `Boolean` |
| `FECHAAPERTURA` | `Date` |
| `FECHACIERRE` | `Date` |
| `FPREVCIERRE` | `Date` |
| `FechaControlEficacia` | `Date` |
| `FechaPrevistaControlEficacia` | `Date` |
| `IDExpediente` | `Integer` |
| `IDNCAsociada` | `Integer` |
| `IDNoConformidad` | `Integer` |
| `IDProyecto` | `Integer` |
| `IDTipo` | `Integer` |
| `Juridica` | `Text` |
| `JuridicaExp` | `Text` |
| `MotivoBorrado` | `Text (Long)` |
| `NOTAS` | `Text (Long)` |
| `Nemotecnico` | `Text` |
| `PROYECTO` | `Text` |
| `RESPONSABLECALIDAD` | `Text` |
| `RESPONSABLECALIDADExp` | `Text` |
| `RESPONSABLETELEFONICA` | `Text` |
| `RequiereACR` | `Boolean` |
| `RequiereControlEficacia` | `Text` |
| `ResponsableEjecucion` | `Text` |
| `ResultadoControlEficacia` | `Text (Long)` |
| `TIPO` | `Text` |
| `Tipologia` | `Text` |
| `VEHICULO` | `Text` |

#### Tabla: `TbNoConformidadesAuditoria`
| Nombre de Columna | Tipo de Dato |
|-------------------|--------------|
| `ACCIONCORRECTIVA` | `Text (Long)` |
| `Borrado` | `Boolean` |
| `CAUSARAIZ` | `Text (Long)` |
| `CORRECCION` | `Text (Long)` |
| `Cerrada` | `Text` |
| `ConformeControlEficacia` | `Text` |
| `ControlEficacia` | `Text (Long)` |
| `DESCRIPCION` | `Text (Long)` |
| `ESTADO` | `Text` |
| `FECHACIERRE` | `Date` |
| `FPREVCIERRE` | `Date` |
| `FechaApertura` | `Date` |
| `FechaControlEficacia` | `Date` |
| `FechaPrevistaControlEficacia` | `Date` |
| `ID` | `Integer` |
| `IDAuditoria` | `Integer` |
| `MotivoBorrado` | `Text (Long)` |
| `MotivoNoAccionCorrectiva` | `Text (Long)` |
| `Notas` | `Text (Long)` |
| `Numero` | `Text` |
| `PuntoNorma` | `Text` |
| `RESPONSABLEIMPLANTACION` | `Text` |
| `RequiereAccionCorrectiva` | `Text` |
| `RequiereControlEficacia` | `Text` |
| `ResultadoControlEficacia` | `Text (Long)` |
| `Tipo` | `Text` |

#### Tabla: `TbNoConformidadesIngresoPorLotesDetalle`
| Nombre de Columna | Tipo de Dato |
|-------------------|--------------|
| `ACCIONCORRECTIVA` | `Text (Long)` |
| `ACCIONREALIZADA` | `Text (Long)` |
| `CAUSA` | `Text (Long)` |
| `CodigoNoConformidad` | `Text` |
| `DESCRIPCION` | `Text (Long)` |
| `DatosDelRegistro` | `Text (Long)` |
| `DocumentoDeReferencia` | `Text (Long)` |
| `ENTIDADRESPONSABLE` | `Text` |
| `EXPEDIENTE` | `Text` |
| `EsNoConformidad` | `Boolean` |
| `FECHAAPERTURA` | `Date` |
| `FECHACIERRE` | `Date` |
| `FECHAPREVISTACIERRE` | `Date` |
| `IDLoteExcel` | `Integer` |
| `NOTAS` | `Text (Long)` |
| `PROYECTO` | `Text` |
| `RESPONSABLETELEFONICA` | `Text` |
| `TIPO` | `Text` |
| `VEHICULO` | `Text` |

#### Tabla: `TbNoConformidadesIngresoPorLotesPrincipal`
| Nombre de Columna | Tipo de Dato |
|-------------------|--------------|
| `FechaRegistro` | `Date` |
| `FilaDatosInicial` | `SmallInt` |
| `IDLoteExcel` | `Integer` |
| `NombreArchivoExcel` | `Text` |
| `Observaciones` | `Text (Long)` |
| `URLCompletaOrigen` | `Text` |

#### Tabla: `TbNoConformidadesIngresoPorLotesTemporal`
| Nombre de Columna | Tipo de Dato |
|-------------------|--------------|
| `ACCIONCORRECTIVATmp` | `Text (Long)` |
| `ACCIONREALIZADATmp` | `Text (Long)` |
| `CAUSATmp` | `Text (Long)` |
| `DESCRIPCIONTmp` | `Text (Long)` |
| `DatosDelRegistroTmp` | `Text (Long)` |
| `DocumentoDeReferenciaTmp` | `Text (Long)` |
| `ENTIDADRESPONSABLETmp` | `Text (Long)` |
| `EXPEDIENTETmp` | `Text (Long)` |
| `EsNoConformidadTmp` | `Text (Long)` |
| `FECHAAPERTURATmp` | `Text (Long)` |
| `FECHACIERRETmp` | `Text (Long)` |
| `FECHAPREVISTACIERRETmp` | `Text (Long)` |
| `IDTmp` | `Integer` |
| `NOTASTmp` | `Text (Long)` |
| `PROYECTOTmp` | `Text (Long)` |
| `RESPONSABLETELEFONICATmp` | `Text (Long)` |
| `TIPOTmp` | `Text (Long)` |
| `VEHICULOTmp` | `Text (Long)` |
| `ValidacionDatos` | `Text (Long)` |
| `blnPasaCriterioParaGrabar` | `Boolean` |

#### Tabla: `TbReplanificacionesAuditoria`
| Nombre de Columna | Tipo de Dato |
|-------------------|--------------|
| `FechaPrevistaAlInicio` | `Date` |
| `FechaPrevistaReplanificada` | `Date` |
| `FechaReprogramacion` | `Date` |
| `IDAccionRealizada` | `Integer` |
| `IDNoConformidad` | `Integer` |
| `IDReplanificacion` | `Integer` |
| `Observaciones` | `Text (Long)` |

#### Tabla: `TbReplanificacionesProyecto`
| Nombre de Columna | Tipo de Dato |
|-------------------|--------------|
| `FechaPrevistaAlInicio` | `Date` |
| `FechaPrevistaReplanificada` | `Date` |
| `FechaReprogramacion` | `Date` |
| `IDAccionRealizada` | `Integer` |
| `IDNoConformidad` | `Integer` |
| `IDReplanificacion` | `Integer` |
| `Observaciones` | `Text (Long)` |

#### Tabla: `TbTareasExplicaciones`
| Nombre de Columna | Tipo de Dato |
|-------------------|--------------|
| `Explicacion` | `Text (Long)` |
| `NodoTarea` | `Text` |
| `TituloTarea` | `Text` |

#### Tabla: `TbTipologia`
| Nombre de Columna | Tipo de Dato |
|-------------------|--------------|
| `CodTipologia` | `Text` |
| `Tipologia` | `Text` |

#### Tabla: `TbTiposNCProyectos`
| Nombre de Columna | Tipo de Dato |
|-------------------|--------------|
| `IDTipo` | `Integer` |
| `Tipologia` | `Text` |

### Tablas Vinculadas (Accesibles)

✅ **Las siguientes tablas están vinculadas a bases de datos externas y son accesibles:**

#### Tabla: `TbExpedientes (VINCULADA ACCESIBLE - c:\Proyectos\scripts-python\dbs-locales\Expedientes_datos.accdb)`
| Nombre de Columna | Tipo de Dato |
|-------------------|--------------|
| `AGEDYSAplica` | `Text` |
| `AGEDYSGenerico` | `Text` |
| `APLICAESTADO` | `Text` |
| `AccesoSharepoint` | `Text (Long)` |
| `Adjudicado` | `Text` |
| `Ambito` | `Text` |
| `AplicaTareaS4H` | `Text` |
| `CadenaPecal` | `Text` |
| `CodExp` | `Text` |
| `CodExpLargo` | `Text` |
| `CodProyecto` | `Text` |
| `CodS4H` | `Text` |
| `CodigoActividad` | `Text` |
| `ContratistaPrincipal` | `Text` |
| `ESTADO` | `Text` |
| `EnPeriodoDeAdjudicacion` | `Text` |
| `EsAM` | `Text` |
| `EsBasado` | `Text` |
| `EsExpediente` | `Text` |
| `EsLote` | `Text` |
| `FECHAADJUDICACION` | `Date` |
| `FECHACERTIFICACION` | `Date` |
| `FECHADESESTIMADA` | `Date` |
| `FECHAFIRMACONTRATO` | `Date` |
| `FECHAINICIOLICITACION` | `Date` |
| `FECHAOFERTA` | `Date` |
| `FECHAPERDIDA` | `Date` |
| `FechaCreacion` | `Date` |
| `FechaFinContrato` | `Date` |
| `FechaFinGarantia` | `Date` |
| `FechaInicioContrato` | `Date` |
| `FechaUltimoCambio` | `Date` |
| `GARANTIAMESES` | `Text` |
| `HPSAplica` | `Text` |
| `IDEjercito` | `Integer` |
| `IDEstado` | `Integer` |
| `IDExpediente` | `Integer` |
| `IDExpedientePadre` | `Integer` |
| `IDOficinaPrograma` | `Integer` |
| `IDOrganoContratacion` | `Integer` |
| `IDResponsableCalidad` | `Integer` |
| `IDUsuarioCreacion` | `Text` |
| `IDUsuarioUltimoCambio` | `Text` |
| `IdGradoClasificacion` | `Integer` |
| `ImporteContratacion` | `Double` |
| `ImporteLicitacion` | `Double` |
| `NPedido` | `Text` |
| `Nemotecnico` | `Text` |
| `Observaciones` | `Text (Long)` |
| `Ordinal` | `Text` |
| `POSTAGEDO` | `Text` |
| `Pecal` | `Text` |
| `Tipo` | `Text` |
| `TipoInforme` | `Text` |
| `Titulo` | `Text (Long)` |

#### Tabla: `TbExpedientesResponsables (VINCULADA ACCESIBLE - c:\Proyectos\scripts-python\dbs-locales\Expedientes_datos.accdb)`
| Nombre de Columna | Tipo de Dato |
|-------------------|--------------|
| `CorreoSiempre` | `Text` |
| `EsJefeProyecto` | `Text` |
| `IDExpedienteResponsable` | `Integer` |
| `IdExpediente` | `Integer` |
| `IdUsuario` | `Integer` |

#### Tabla: `TbNoConformidades1 (VINCULADA ACCESIBLE - c:\Proyectos\scripts-python\dbs-locales\NoConformidades_Datos.accdb)`
| Nombre de Columna | Tipo de Dato |
|-------------------|--------------|
| `ACR` | `Text (Long)` |
| `Borrado` | `Boolean` |
| `CAUSA` | `Text (Long)` |
| `CausaYAnalisRaiz` | `Text (Long)` |
| `Cerrada` | `Text` |
| `CodConcesionAsociada` | `Text` |
| `CodExp` | `Text` |
| `CodigoNoConformidad` | `Text` |
| `CodigoNoConformidadAsociada` | `Text` |
| `CodigoRiesgo` | `Text` |
| `ConformeControlEficacia` | `Text` |
| `ControlEficacia` | `Text (Long)` |
| `DESCRIPCION` | `Text (Long)` |
| `DetectadoPor` | `Text` |
| `ENTIDADRESPONSABLE` | `Text` |
| `ESTADO` | `Text` |
| `EXPEDIENTE` | `Text` |
| `EsNoConformidad` | `Boolean` |
| `FECHAAPERTURA` | `Date` |
| `FECHACIERRE` | `Date` |
| `FPREVCIERRE` | `Date` |
| `FechaControlEficacia` | `Date` |
| `FechaPrevistaControlEficacia` | `Date` |
| `IDExpediente` | `Integer` |
| `IDNCAsociada` | `Integer` |
| `IDNoConformidad` | `Integer` |
| `IDProyecto` | `Integer` |
| `IDTipo` | `Integer` |
| `Juridica` | `Text` |
| `JuridicaExp` | `Text` |
| `MotivoBorrado` | `Text (Long)` |
| `NOTAS` | `Text (Long)` |
| `Nemotecnico` | `Text` |
| `PROYECTO` | `Text` |
| `RESPONSABLECALIDAD` | `Text` |
| `RESPONSABLECALIDADExp` | `Text` |
| `RESPONSABLETELEFONICA` | `Text` |
| `RequiereACR` | `Boolean` |
| `RequiereControlEficacia` | `Text` |
| `ResponsableEjecucion` | `Text` |
| `ResultadoControlEficacia` | `Text (Long)` |
| `TIPO` | `Text` |
| `Tipologia` | `Text` |
| `VEHICULO` | `Text` |

#### Tabla: `TbRiesgos (VINCULADA ACCESIBLE - c:\Proyectos\scripts-python\dbs-locales\Gestion_Riesgos_Datos.accdb)`
| Nombre de Columna | Tipo de Dato |
|-------------------|--------------|
| `Calidad` | `Text` |
| `CausaRaiz` | `Text (Long)` |
| `CodRiesgoBiblioteca` | `Text` |
| `CodigoRiesgo` | `Text` |
| `CodigoUnico` | `Text` |
| `ColorIcono` | `Text` |
| `Contingencia` | `Text` |
| `Coste` | `Text` |
| `Descripcion` | `Text (Long)` |
| `DetectadoPor` | `Text` |
| `DiasSinRespuestaCalidadAceptacion` | `Text` |
| `DiasSinRespuestaCalidadRetipificacion` | `Text` |
| `DiasSinRespuestaCalidadRetiro` | `Text` |
| `EntidadDetecta` | `Text` |
| `Estado` | `Text` |
| `FechaAprobacionAceptacionPorCalidad` | `Date` |
| `FechaAprobacionRetiroPorCalidad` | `Date` |
| `FechaCerrado` | `Date` |
| `FechaDetectado` | `Date` |
| `FechaEstado` | `Text` |
| `FechaJustificacionAceptacionRiesgo` | `Date` |
| `FechaJustificacionRetiroRiesgo` | `Date` |
| `FechaMaterializado` | `Date` |
| `FechaMitigacionAceptar` | `Date` |
| `FechaRechazoAceptacionPorCalidad` | `Date` |
| `FechaRechazoRetiroPorCalidad` | `Date` |
| `FechaRetirado` | `Date` |
| `FechaRiesgoParaRetipificar` | `Date` |
| `FechaRiesgoRetipificado` | `Date` |
| `HayErrorEnRiesgo` | `Text` |
| `IDEdicion` | `Integer` |
| `IDRiesgo` | `Integer` |
| `ImpactoGlobal` | `Text` |
| `JustificacionAceptacionRiesgo` | `Text (Long)` |
| `JustificacionRetiroRiesgo` | `Text (Long)` |
| `Mitigacion` | `Text` |
| `NombreIcono` | `Text` |
| `NombreNodoDesc` | `Text` |
| `NombreNodoEstado` | `Text` |
| `Origen` | `Text` |
| `Plazo` | `Text` |
| `Priorizacion` | `SmallInt` |
| `RequierePlanContingencia` | `Text` |
| `RequiereRiesgoDeBiblioteca` | `Text` |
| `RiesgoPendienteRetipificacion` | `Text` |
| `Valoracion` | `Text` |
| `Vulnerabilidad` | `Text` |

#### Tabla: `TbRiesgosNC (VINCULADA ACCESIBLE - c:\Proyectos\scripts-python\dbs-locales\Gestion_Riesgos_Datos.accdb)`
| Nombre de Columna | Tipo de Dato |
|-------------------|--------------|
| `FechaDecison` | `Date` |
| `FechaRegistro` | `Date` |
| `ID` | `Integer` |
| `IDNC` | `Integer` |
| `IDRiesgo` | `Integer` |
| `ParaNC` | `Text` |

#### Tabla: `TbUsuariosAplicaciones (VINCULADA ACCESIBLE - c:\Proyectos\scripts-python\dbs-locales\Lanzadera_Datos.accdb)`
| Nombre de Columna | Tipo de Dato |
|-------------------|--------------|
| `Activado` | `Boolean` |
| `CorreoUsuario` | `Text` |
| `EsAdministrador` | `Text` |
| `FechaAlta` | `Date` |
| `FechaBaja` | `Date` |
| `FechaBloqueo` | `Date` |
| `FechaProximoCambioContrasenia` | `Date` |
| `FechaUltimaConexion` | `Date` |
| `Id` | `SmallInt` |
| `JefeDelUsuario` | `Text` |
| `MantenerLanzaderaAbierta` | `Boolean` |
| `Matricula` | `Text` |
| `Movil` | `Text` |
| `Nombre` | `Text` |
| `Observaciones` | `Text (Long)` |
| `ParaTareasProgramadas` | `Boolean` |
| `PassIncialPlana` | `Text` |
| `Password` | `Text` |
| `PasswordNuncaCaduca` | `Boolean` |
| `PermisoPruebas` | `Text` |
| `PermisosAsignados` | `Boolean` |
| `Telefono` | `Text` |
| `TieneQueCambiarLaContrasenia` | `Boolean` |
| `UsuarioImborrable` | `Boolean` |
| `UsuarioRed` | `Text` |
| `UsuarioSSID` | `Text` |

### Tablas Vinculadas (No Accesibles)

⚠️ **Las siguientes tablas están vinculadas a bases de datos externas que no están disponibles:**

#### Tabla: `TbCorreosEnviados (VINCULADA NO ACCESIBLE - \\datoste\Aplicaciones_dys\Aplicaciones PpD\00Recursos\Tareas_datos.accdb)`
| Información | Detalle |
|-------------|----------|
| Tipo | Tabla Vinculada |
| Ruta Esperada | `\\datoste\Aplicaciones_dys\Aplicaciones PpD\00Recursos\Tareas_datos.accdb` |
| Estado | NO ACCESIBLE |

## Relaciones entre Tablas

Las siguientes relaciones fueron encontradas en el esquema de la base de datos:

- La tabla `TbAnexos.IDNoConformidad` se relaciona con `TbNoConformidades.IDNoConformidad`.
- La tabla `TbDocumentosAuditorias.IDAuditoria` se relaciona con `TbAuditorias.IDAuditoria`.
- La tabla `TbDocumentosAuditorias.IDAccionRealizada` se relaciona con `TbNCAuditoriaAccionesRealizadas.IDAccionRealizada`.
- La tabla `TbDocumentosAuditorias.IDNoConformidad` se relaciona con `TbNoConformidadesAuditoria.ID`.
- La tabla `TbNCAccionCorrectivas.IDNoConformidad` se relaciona con `TbNoConformidades.IDNoConformidad`.
- La tabla `TbNCAccionesRealizadas.IDAccionCorrectiva` se relaciona con `TbNCAccionCorrectivas.IDAccionCorrectiva`.
- La tabla `TbNCAuditoriaAccionCorrectivas.ID` se relaciona con `TbNoConformidadesAuditoria.ID`.
- La tabla `TbNCAuditoriaAccionesRealizadas.IDAccionCorrectiva` se relaciona con `TbNCAuditoriaAccionCorrectivas.IDAccionCorrectiva`.
- La tabla `TbNCDocumentos.IDNoConformidad` se relaciona con `TbNoConformidades.IDNoConformidad`.
- La tabla `TbNCInformacionRAC.IDNoConformidad` se relaciona con `TbNoConformidades.IDNoConformidad`.
- La tabla `TbNCInformacionRACAnexos.IDInformacionRAC` se relaciona con `TbNCInformacionRAC.IDInformacionRAC`.
- La tabla `TbNoConformidadesAuditoria.IDAuditoria` se relaciona con `TbAuditorias.IDAuditoria`.
- La tabla `TbReplanificacionesProyecto.IDAccionRealizada` se relaciona con `TbNCAccionesRealizadas.IDAccionRealizada`.
