add_library(pdfium_fxjs OBJECT EXCLUDE_FROM_ALL
    "${PDFIUM_ROOT}/fxjs/cjs_event_context_stub.cpp"
    "${PDFIUM_ROOT}/fxjs/cjs_event_context_stub.h"
    "${PDFIUM_ROOT}/fxjs/cjs_runtimestub.cpp"
    "${PDFIUM_ROOT}/fxjs/cjs_runtimestub.h"
    "${PDFIUM_ROOT}/fxjs/ijs_event_context.h"
    "${PDFIUM_ROOT}/fxjs/ijs_runtime.cpp"
    "${PDFIUM_ROOT}/fxjs/ijs_runtime.h"
)
add_library(pdfium::fxjs ALIAS pdfium_fxjs)
target_link_libraries(pdfium_fxjs
    PRIVATE
        pdfium::strict_config
    PUBLIC
        pdfium::core_fxcrt
)
if(PDF_ENABLE_V8)
    target_sources(pdfium_fxjs PRIVATE
        "${PDFIUM_ROOT}/fxjs/cfx_globaldata.cpp"
        "${PDFIUM_ROOT}/fxjs/cfx_globaldata.h"
        "${PDFIUM_ROOT}/fxjs/cfx_keyvalue.cpp"
        "${PDFIUM_ROOT}/fxjs/cfx_keyvalue.h"
        "${PDFIUM_ROOT}/fxjs/cfx_v8.cpp"
        "${PDFIUM_ROOT}/fxjs/cfx_v8.h"
        "${PDFIUM_ROOT}/fxjs/cfxjs_engine.cpp"
        "${PDFIUM_ROOT}/fxjs/cfxjs_engine.h"
        "${PDFIUM_ROOT}/fxjs/cjs_annot.cpp"
        "${PDFIUM_ROOT}/fxjs/cjs_annot.h"
        "${PDFIUM_ROOT}/fxjs/cjs_app.cpp"
        "${PDFIUM_ROOT}/fxjs/cjs_app.h"
        "${PDFIUM_ROOT}/fxjs/cjs_border.cpp"
        "${PDFIUM_ROOT}/fxjs/cjs_border.h"
        "${PDFIUM_ROOT}/fxjs/cjs_color.cpp"
        "${PDFIUM_ROOT}/fxjs/cjs_color.h"
        "${PDFIUM_ROOT}/fxjs/cjs_console.cpp"
        "${PDFIUM_ROOT}/fxjs/cjs_console.h"
        "${PDFIUM_ROOT}/fxjs/cjs_delaydata.cpp"
        "${PDFIUM_ROOT}/fxjs/cjs_delaydata.h"
        "${PDFIUM_ROOT}/fxjs/cjs_display.cpp"
        "${PDFIUM_ROOT}/fxjs/cjs_display.h"
        "${PDFIUM_ROOT}/fxjs/cjs_document.cpp"
        "${PDFIUM_ROOT}/fxjs/cjs_document.h"
        "${PDFIUM_ROOT}/fxjs/cjs_event.cpp"
        "${PDFIUM_ROOT}/fxjs/cjs_event.h"
        "${PDFIUM_ROOT}/fxjs/cjs_event_context.cpp"
        "${PDFIUM_ROOT}/fxjs/cjs_event_context.h"
        "${PDFIUM_ROOT}/fxjs/cjs_eventrecorder.cpp"
        "${PDFIUM_ROOT}/fxjs/cjs_eventrecorder.h"
        "${PDFIUM_ROOT}/fxjs/cjs_field.cpp"
        "${PDFIUM_ROOT}/fxjs/cjs_field.h"
        "${PDFIUM_ROOT}/fxjs/cjs_font.cpp"
        "${PDFIUM_ROOT}/fxjs/cjs_font.h"
        "${PDFIUM_ROOT}/fxjs/cjs_global.cpp"
        "${PDFIUM_ROOT}/fxjs/cjs_global.h"
        "${PDFIUM_ROOT}/fxjs/cjs_globalarrays.cpp"
        "${PDFIUM_ROOT}/fxjs/cjs_globalarrays.h"
        "${PDFIUM_ROOT}/fxjs/cjs_globalconsts.cpp"
        "${PDFIUM_ROOT}/fxjs/cjs_globalconsts.h"
        "${PDFIUM_ROOT}/fxjs/cjs_highlight.cpp"
        "${PDFIUM_ROOT}/fxjs/cjs_highlight.h"
        "${PDFIUM_ROOT}/fxjs/cjs_icon.cpp"
        "${PDFIUM_ROOT}/fxjs/cjs_icon.h"
        "${PDFIUM_ROOT}/fxjs/cjs_object.cpp"
        "${PDFIUM_ROOT}/fxjs/cjs_object.h"
        "${PDFIUM_ROOT}/fxjs/cjs_position.cpp"
        "${PDFIUM_ROOT}/fxjs/cjs_position.h"
        "${PDFIUM_ROOT}/fxjs/cjs_publicmethods.cpp"
        "${PDFIUM_ROOT}/fxjs/cjs_publicmethods.h"
        "${PDFIUM_ROOT}/fxjs/cjs_result.cpp"
        "${PDFIUM_ROOT}/fxjs/cjs_result.h"
        "${PDFIUM_ROOT}/fxjs/cjs_runtime.cpp"
        "${PDFIUM_ROOT}/fxjs/cjs_runtime.h"
        "${PDFIUM_ROOT}/fxjs/cjs_scalehow.cpp"
        "${PDFIUM_ROOT}/fxjs/cjs_scalehow.h"
        "${PDFIUM_ROOT}/fxjs/cjs_scalewhen.cpp"
        "${PDFIUM_ROOT}/fxjs/cjs_scalewhen.h"
        "${PDFIUM_ROOT}/fxjs/cjs_style.cpp"
        "${PDFIUM_ROOT}/fxjs/cjs_style.h"
        "${PDFIUM_ROOT}/fxjs/cjs_timerobj.cpp"
        "${PDFIUM_ROOT}/fxjs/cjs_timerobj.h"
        "${PDFIUM_ROOT}/fxjs/cjs_util.cpp"
        "${PDFIUM_ROOT}/fxjs/cjs_util.h"
        "${PDFIUM_ROOT}/fxjs/cjs_zoomtype.cpp"
        "${PDFIUM_ROOT}/fxjs/cjs_zoomtype.h"
        "${PDFIUM_ROOT}/fxjs/fx_date_helpers.cpp"
        "${PDFIUM_ROOT}/fxjs/fx_date_helpers.h"
        "${PDFIUM_ROOT}/fxjs/fxv8.cpp"
        "${PDFIUM_ROOT}/fxjs/fxv8.h"
        "${PDFIUM_ROOT}/fxjs/global_timer.cpp"
        "${PDFIUM_ROOT}/fxjs/global_timer.h"
        "${PDFIUM_ROOT}/fxjs/js_define.cpp"
        "${PDFIUM_ROOT}/fxjs/js_define.h"
        "${PDFIUM_ROOT}/fxjs/js_resources.cpp"
        "${PDFIUM_ROOT}/fxjs/js_resources.h"
    )
    find_packge(v8 REQUIRED)
    target_link_libraries(pdfium_fxjs
        PUBLIC
            pdfium::constants
            pdfium::core_fdrm
            pdfium::core_fpdfapi_page
            pdfium::core_fpdfapi_parser
            pdfium::core_fpdfapi_render
            pdfium::core_fpdfdoc
            pdfium::core_fxge
            v8::v8  # FIXME: imported v8
    )
    if(PDF_ENABLE_XFA)
        target_sources(pdfium_fxjs PRIVATE
            "${PDFIUM_ROOT}/fxjs/xfa/cfxjse_class.cpp"
            "${PDFIUM_ROOT}/fxjs/xfa/cfxjse_class.h"
            "${PDFIUM_ROOT}/fxjs/xfa/cfxjse_context.cpp"
            "${PDFIUM_ROOT}/fxjs/xfa/cfxjse_context.h"
            "${PDFIUM_ROOT}/fxjs/xfa/cfxjse_engine.cpp"
            "${PDFIUM_ROOT}/fxjs/xfa/cfxjse_engine.h"
            "${PDFIUM_ROOT}/fxjs/xfa/cfxjse_formcalc_context.cpp"
            "${PDFIUM_ROOT}/fxjs/xfa/cfxjse_formcalc_context.h"
            "${PDFIUM_ROOT}/fxjs/xfa/cfxjse_isolatetracker.cpp"
            "${PDFIUM_ROOT}/fxjs/xfa/cfxjse_isolatetracker.h"
            "${PDFIUM_ROOT}/fxjs/xfa/cfxjse_mapmodule.cpp"
            "${PDFIUM_ROOT}/fxjs/xfa/cfxjse_mapmodule.h"
            "${PDFIUM_ROOT}/fxjs/xfa/cfxjse_nodehelper.cpp"
            "${PDFIUM_ROOT}/fxjs/xfa/cfxjse_nodehelper.h"
            "${PDFIUM_ROOT}/fxjs/xfa/cfxjse_resolveprocessor.cpp"
            "${PDFIUM_ROOT}/fxjs/xfa/cfxjse_resolveprocessor.h"
            "${PDFIUM_ROOT}/fxjs/xfa/cfxjse_runtimedata.cpp"
            "${PDFIUM_ROOT}/fxjs/xfa/cfxjse_runtimedata.h"
            "${PDFIUM_ROOT}/fxjs/xfa/cfxjse_value.cpp"
            "${PDFIUM_ROOT}/fxjs/xfa/cfxjse_value.h"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_boolean.cpp"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_boolean.h"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_container.cpp"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_container.h"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_datawindow.cpp"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_datawindow.h"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_delta.cpp"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_delta.h"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_desc.cpp"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_desc.h"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_draw.cpp"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_draw.h"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_encrypt.cpp"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_encrypt.h"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_eventpseudomodel.cpp"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_eventpseudomodel.h"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_exclgroup.cpp"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_exclgroup.h"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_extras.cpp"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_extras.h"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_field.cpp"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_field.h"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_form.cpp"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_form.h"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_handler.cpp"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_handler.h"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_hostpseudomodel.cpp"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_hostpseudomodel.h"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_instancemanager.cpp"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_instancemanager.h"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_layoutpseudomodel.cpp"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_layoutpseudomodel.h"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_list.cpp"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_list.h"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_logpseudomodel.cpp"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_logpseudomodel.h"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_manifest.cpp"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_manifest.h"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_model.cpp"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_model.h"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_node.cpp"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_node.h"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_object.cpp"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_object.h"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_occur.cpp"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_occur.h"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_packet.cpp"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_packet.h"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_script.cpp"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_script.h"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_signaturepseudomodel.cpp"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_signaturepseudomodel.h"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_source.cpp"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_source.h"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_subform.cpp"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_subform.h"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_template.cpp"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_template.h"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_textnode.cpp"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_textnode.h"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_tree.cpp"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_tree.h"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_treelist.cpp"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_treelist.h"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_wsdlconnection.cpp"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_wsdlconnection.h"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_xfa.cpp"
            "${PDFIUM_ROOT}/fxjs/xfa/cjx_xfa.h"
            "${PDFIUM_ROOT}/fxjs/xfa/fxjse.cpp"
            "${PDFIUM_ROOT}/fxjs/xfa/fxjse.h"
            "${PDFIUM_ROOT}/fxjs/xfa/jse_define.h"
            $<TARGET_OBJECTS:pdfium_fxjs_gc>
        )
        target_link_libraries(pdfium_fxjs
            PUBLCI
                pdfium::xfa_fgas_crt
                pdfium::xfa_fgas_fm2js
        )
    endif()
endif()
if(PDF_ENABLE_V8)
    if(PDF_ENABLE_XFA)
        add_library(pdfium_fxjs_gc OBJECT EXCLUDE_FROM_ALL
            "${PDFIUM_ROOT}/fxjs/gc/container_trace.h"
            "${PDFIUM_ROOT}/fxjs/gc/gced_tree_node.h"
            "${PDFIUM_ROOT}/fxjs/gc/gced_tree_node_mixin.h"
            "${PDFIUM_ROOT}/fxjs/gc/heap.cpp"
            "${PDFIUM_ROOT}/fxjs/gc/heap.h"
        )
        add_library(pdfium::fxjs_gc ALIAS pdfium_fxjs_gc)
        target_link_libraries(pdfium_fxjs_gx
            PRIVATE
                pdfium::strict_config
            PUBLIC
                pdfium::core_fxcrt
                pdfium::v8_libplatform
        )
    endif()
endif()
