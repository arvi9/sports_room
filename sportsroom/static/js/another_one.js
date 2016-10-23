/**
 * Created by athul on 23/10/16.
 */
function do_action(action) {
    $('div.actions option[selected]').attr('selected', '');
    $('div.actions option[value='+action+']').attr('selected', 'selected');
    $("div.actions").parent().submit();
}

function fix_actions() {
    $('th.action-checkbox-column:first').prepend('select<br />all<br />');
    if ($('div.actions option:gt(0)').length<=8) { // Only do this for short lists. Probably need to tweak this number.

        $('div.actions label, div.actions button').hide();
        actions_html='<div id="action_buttons" style="padding: 2px 0 2px 0;">';
        $('div.actions option:gt(0)').each(function(i) {
            actions_html+='<a href="javascript:void(0);" onclick="do_action(\''+this.value+'\');">'+this.text+'</a>';
        });
        actions_html+='</div>';
        $('div.actions').append(actions_html);
    }
}
